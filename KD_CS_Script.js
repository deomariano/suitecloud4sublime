/** 
 *  Copyright (c) 2019 Kodella, LLC. All rights reserved.
 *
 *  The following code is protected by US and International copyright laws.     
 *  Reproduction and distribution of this code without written permission
 *  from Kodella, LLC is prohibited.
 *  
 *  Version     Date        Author      Remarks
 *  1.00                    Kodella     Initial version
 *  
 *  Description
 *  Script Description goes here.
 *
 *  @NScriptType ClientScript
 *  @NApiVersion 2.x
 *
 */
define(['N/record'], function(record) {

    function pageInit(context) {

    }

    function fieldChanged(context) {

    }

    function validateField(context) {

        return true;
    }

    function postSourcing(context) {

    }

    function lineInit(context) {

    }

    function validateLine(context) {

        return true;
    }

    function validateInsert(context) {

        return true;
    }

    function validateDelete(context) {

        return true;
    }

    function sublistChanged(context) {

    }

    function saveRecord(context) {

        return true;
    }

    return {
        beforeLoad: beforeLoad,
        beforeSubmit: beforeSubmit,
        afterSubmit: afterSubmit
    }

})