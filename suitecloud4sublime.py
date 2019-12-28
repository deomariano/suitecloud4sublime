import sublime
import sublime_plugin
import json
import ntpath

try:
    from urllib.request import Request, urlopen
except ImportError:
    from urllib2 import Request, urlopen

configSettings = sublime.load_settings("config.sublime-settings")

class TestCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		print(configSettings.get("savefilebeforeupload"))

class GenerateUeCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		n = self.view.window().new_file()
		p = sublime.find_resources("ue.template")
		n.insert(edit, 0, sublime.load_resource(p[0]).replace('\r\n', '\n'))

class GenerateCsCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		n = self.view.window().new_file()
		p = sublime.find_resources("cs.template")
		n.insert(edit, 0, sublime.load_resource(p[0]).replace('\r\n', '\n'))

class GenerateSlCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		n = self.view.window().new_file()
		p = sublime.find_resources("sl.template")
		n.insert(edit, 0, sublime.load_resource(p[0]).replace('\r\n', '\n'))

class GenerateRlCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		n = self.view.window().new_file()
		p = sublime.find_resources("rl.template")
		n.insert(edit, 0, sublime.load_resource(p[0]).replace('\r\n', '\n'))

class GenerateMrCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		n = self.view.window().new_file()
		p = sublime.find_resources("mr.template")
		n.insert(edit, 0, sublime.load_resource(p[0]).replace('\r\n', '\n'))

class GenerateSsCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		n = self.view.window().new_file()
		p = sublime.find_resources("ss.template")
		n.insert(edit, 0, sublime.load_resource(p[0]).replace('\r\n', '\n'))

class GenerateMuCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		n = self.view.window().new_file()
		p = sublime.find_resources("mu.template")
		n.insert(edit, 0, sublime.load_resource(p[0]).replace('\r\n', '\n'))

class GeneratePlCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		n = self.view.window().new_file()
		p = sublime.find_resources("pl.template")
		n.insert(edit, 0, sublime.load_resource(p[0]).replace('\r\n', '\n'))

class GenerateWaCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		n = self.view.window().new_file()
		p = sublime.find_resources("wa.template")
		n.insert(edit, 0, sublime.load_resource(p[0]).replace('\r\n', '\n'))

class PreferencesCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		self.view.window().open_file("config.sublime-settings")

class UploadFileCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		if configSettings.get("savefilebeforeupload"): 
			self.view.run_command("save")

		fileData = self.view.substr(sublime.Region(0, self.view.size()))
		fileName = ntpath.basename(self.view.file_name())

		if fileName:
			try:
				req = Request(configSettings.get("restlet"))
				req.add_header("Authorization", "NLAuth nlauth_email=%s, nlauth_signature=%s, nlauth_account=%s, nlauth_role=%s" % (configSettings.get("email_address"), configSettings.get("password"), configSettings.get("account"), configSettings.get("role")))
				req.add_header("Content-Type", "application/json")
				req.data = json.dumps({
					"folder": configSettings.get("folder"),
					"filename": fileName,
					"fileContent": fileData,
					"action": "upload"
				}).encode("utf-8")
				response = urlopen(req).read().decode("utf-8")
				responseObj = json.loads(response)
				sublime.message_dialog(responseObj["message"])
			except TypeError as err: 
				sublime.error_message("Test Connection Failed: \n" + str(err))
			except HTTPError as err:
				sublime.error_message("Test Connection Failed: \n" + str(err))
			except:
				sublime.error_message("Upload Failed due to an unexpected error! :(")
		else:
			sublime.error_message("Please save the file first.")

class DownloadFileCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		region = sublime.Region(0, self.view.size())
		fileName = ntpath.basename(self.view.file_name())

		if fileName:
			try:
				req = Request(configSettings.get("restlet"))
				req.add_header("Authorization", "NLAuth nlauth_email=%s, nlauth_signature=%s, nlauth_account=%s, nlauth_role=%s" % (configSettings.get("email_address"), configSettings.get("password"), configSettings.get("account"), configSettings.get("role")))
				req.add_header("Content-Type", "application/json")
				req.data = json.dumps({
					"folder": configSettings.get("folder"),
					"filename": fileName,
					"action": "download"
				}).encode("utf-8")
				response = urlopen(req).read().decode("utf-8")
				responseObj = json.loads(response)
				sublime.message_dialog(responseObj["message"])

				if responseObj["status"] == "Success":
					self.view.replace(edit, region, responseObj["data"])

			except TypeError as err: 
				sublime.error_message("Test Connection Failed: \n" + str(err))
			except HTTPError as err:
				sublime.error_message("Test Connection Failed: \n" + str(err))
			except:
				sublime.error_message("Download Failed due to an unexpected error! :(")
		else:
			sublime.error_message("Please save the file first.")

class CompareFilesCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		thisFileUrl = self.view.file_name()
		fileName = ntpath.basename(self.view.file_name())

		otherFileView = self.view.window().open_file("tempfile")
		otherFileUrl = otherFileView.file_name()
		otherFileRegion = sublime.Region(0, otherFileView.size())

		if fileName:
			try:
				req = Request(configSettings.get("restlet"))
				req.add_header("Authorization", "NLAuth nlauth_email=%s, nlauth_signature=%s, nlauth_account=%s, nlauth_role=%s" % (configSettings.get("email_address"), configSettings.get("password"), configSettings.get("account"), configSettings.get("role")))
				req.add_header("Content-Type", "application/json")
				req.data = json.dumps({
					"folder": configSettings.get("folder"),
					"filename": fileName,
					"action": "download"
				}).encode("utf-8")
				response = urlopen(req).read().decode("utf-8")
				responseObj = json.loads(response)
				if responseObj["status"] == "Success":

					otherFileView.replace(edit, otherFileRegion, responseObj["data"])
					otherFileView.run_command("save")
					otherFileView.window().run_command("close")

					self.view.window().run_command('diff_files', {"files": [thisFileUrl, otherFileUrl]})

					otherFileView.replace(edit, otherFileRegion, "")
					otherFileView.run_command("save")

			except TypeError as err: 
				sublime.error_message("Test Connection Failed: \n" + str(err))
			except HTTPError as err:
				sublime.error_message("Test Connection Failed: \n" + str(err))
			except:
				sublime.error_message("Compare Failed due to an unexpected error! :(")
		else:
			sublime.error_message("Please save the file first.")

class TestIntegrationCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		try:
			req = Request(configSettings.get("restlet"))
			req.add_header("Authorization", "NLAuth nlauth_email=%s, nlauth_signature=%s, nlauth_account=%s, nlauth_role=%s" % (configSettings.get("email_address"), configSettings.get("password"), configSettings.get("account"), configSettings.get("role")))
			req.add_header("Content-Type", "application/json")
			response = urlopen(req).read().decode("utf-8")
			responseObj = json.loads(response)
			sublime.message_dialog(responseObj["message"])
		except TypeError as err: 
			sublime.error_message("Test Connection Failed: \n" + str(err))
		except HTTPError as err:
			sublime.error_message("Test Connection Failed: \n" + str(err))
		except:
			sublime.error_message("Test Connection Failed due to an unexpected error! :(")
