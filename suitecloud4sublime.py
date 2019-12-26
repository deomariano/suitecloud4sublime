import sublime
import sublime_plugin
import json
import ntpath

try:
    from urllib.request import Request, urlopen
except ImportError:
    from urllib2 import Request, urlopen

class GenerateUeCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		n = self.view.window().new_file()
		n.insert(edit, 0, sublime.load_resource("Packages/suitecloud4sublime/KD_UE_Script.js").replace('\r\n', '\n'))

class GenerateCsCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		n = self.view.window().new_file()
		n.insert(edit, 0, sublime.load_resource("Packages/suitecloud4sublime/KD_CS_Script.js").replace('\r\n', '\n'))

class GenerateSlCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		n = self.view.window().new_file()
		n.insert(edit, 0, sublime.load_resource("Packages/suitecloud4sublime/KD_SL_Script.js").replace('\r\n', '\n'))

class GenerateRlCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		n = self.view.window().new_file()
		n.insert(edit, 0, sublime.load_resource("Packages/suitecloud4sublime/KD_RL_Script.js").replace('\r\n', '\n'))

class GenerateMrCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		n = self.view.window().new_file()
		n.insert(edit, 0, sublime.load_resource("Packages/suitecloud4sublime/KD_MR_Script.js").replace('\r\n', '\n'))

class GenerateSsCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		n = self.view.window().new_file()
		n.insert(edit, 0, sublime.load_resource("Packages/suitecloud4sublime/KD_SS_Script.js").replace('\r\n', '\n'))

class GenerateMuCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		n = self.view.window().new_file()
		n.insert(edit, 0, sublime.load_resource("Packages/suitecloud4sublime/KD_MU_Script.js").replace('\r\n', '\n'))

class GeneratePlCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		n = self.view.window().new_file()
		n.insert(edit, 0, sublime.load_resource("Packages/suitecloud4sublime/KD_PL_Script.js").replace('\r\n', '\n'))

class GenerateWaCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		n = self.view.window().new_file()
		n.insert(edit, 0, sublime.load_resource("Packages/suitecloud4sublime/KD_WA_Script.js").replace('\r\n', '\n'))

class PreferencesCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		self.view.window().open_file("config.sublime-settings")

class UploadFileCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		configFile = sublime.load_resource("Packages/config.sublime-settings")
		configObj = sublime.decode_value(configFile)
		fileData = self.view.substr(sublime.Region(0, self.view.size()))
		fileName = ntpath.basename(self.view.file_name())

		if fileName:
			try:
				req = Request(configObj["restlet"])
				req.add_header("Authorization", "NLAuth nlauth_email=%s, nlauth_signature=%s, nlauth_account=%s, nlauth_role=%s" % (configObj["email_address"], configObj["password"], configObj["account"], configObj["role"]))
				req.add_header("Content-Type", "application/json")
				req.data = json.dumps({
					"folder": configObj["folder"],
					"filename": fileName,
					"fileContent": fileData,
					"action": "upload"
				}).encode("utf-8")
				response = urlopen(req).read().decode("utf-8")
				responseObj = json.loads(response)
				sublime.message_dialog(responseObj["message"])
			except TypeError as err: 
				sublime.error_message("Upload Failed: \n" + str(err))
			except URLError as err:
				sublime.error_message("Upload Failed: \n" + str(err))
			except:
				sublime.error_message("Upload Failed due to an unexpected error! :(")
		else:
			sublime.error_message("Please save the file first.")

class DownloadFileCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		configFile = sublime.load_resource("Packages/config.sublime-settings")
		configObj = sublime.decode_value(configFile)
		region = sublime.Region(0, self.view.size())
		fileName = ntpath.basename(self.view.file_name())

		if fileName:
			try:
				req = Request(configObj["restlet"])
				req.add_header("Authorization", "NLAuth nlauth_email=%s, nlauth_signature=%s, nlauth_account=%s, nlauth_role=%s" % (configObj["email_address"], configObj["password"], configObj["account"], configObj["role"]))
				req.add_header("Content-Type", "application/json")
				req.data = json.dumps({
					"folder": configObj["folder"],
					"filename": fileName,
					"action": "download"
				}).encode("utf-8")
				response = urlopen(req).read().decode("utf-8")
				responseObj = json.loads(response)
				sublime.message_dialog(responseObj["message"])

				if responseObj["status"] == "Success":
					self.view.replace(edit, region, responseObj["data"])

			except TypeError as err: 
				sublime.error_message("Download Failed: \n" + str(err))
			except URLError as err:
				sublime.error_message("Download Failed: \n" + str(err))
			except:
				sublime.error_message("Download Failed due to an unexpected error! :(")
		else:
			sublime.error_message("Please save the file first.")


class TestIntegrationCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		configFile = sublime.load_resource("Packages/config.sublime-settings")
		configObj = sublime.decode_value(configFile)

		try:
			req = Request(configObj["restlet"])
			req.add_header("Authorization", "NLAuth nlauth_email=%s, nlauth_signature=%s, nlauth_account=%s, nlauth_role=%s" % (configObj["email_address"], configObj["password"], configObj["account"], configObj["role"]))
			req.add_header("Content-Type", "application/json")
			response = urlopen(req).read().decode("utf-8")
			responseObj = json.loads(response)
			sublime.message_dialog(responseObj["message"])
		except TypeError as err: 
			sublime.error_message("Test Connection Failed: \n" + str(err))
		except URLError as err:
			sublime.error_message("Test Connection Failed: \n" + str(err))
		except:
			sublime.error_message("Test Connection Failed due to an unexpected error! :(")

