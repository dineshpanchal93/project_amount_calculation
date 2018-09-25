# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "project_amount_calculation"
app_title = "Project Amount Calculation"
app_publisher = "info@progressiveit.in"
app_description = "Adding Stock Entry and Journal Entry Amounts in Project"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "info@progressiveit.in"
app_license = "MIT"


fixtures = ["Custom Field"]
# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/project_amount_calculation/css/project_amount_calculation.css"
# app_include_js = "/assets/project_amount_calculation/js/project_amount_calculation.js"

# include js, css files in header of web template
# web_include_css = "/assets/project_amount_calculation/css/project_amount_calculation.css"
# web_include_js = "/assets/project_amount_calculation/js/project_amount_calculation.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "project_amount_calculation.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "project_amount_calculation.install.before_install"
# after_install = "project_amount_calculation.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "project_amount_calculation.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }
doc_events = {
	
	"Project" : {
		"validate" : ["project_amount_calculation.project_amount_calculation.project_custom.update_amount","project_amount_calculation.project_amount_calculation.project_custom.update_stock_amount",
                "project_amount_calculation.project_amount_calculation.project_custom.update_journal_amount" ]
		
		
	}

	

}
# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"project_amount_calculation.tasks.all"
# 	],
# 	"daily": [
# 		"project_amount_calculation.tasks.daily"
# 	],
# 	"hourly": [
# 		"project_amount_calculation.tasks.hourly"
# 	],
# 	"weekly": [
# 		"project_amount_calculation.tasks.weekly"
# 	]
# 	"monthly": [
# 		"project_amount_calculation.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "project_amount_calculation.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "project_amount_calculation.event.get_events"
# }

