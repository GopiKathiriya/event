import frappe



@frappe.whitelist()
def get_permission_query_for_examresult(user=None):
    if not user:
        user = frappe.session.user
    user_roles = frappe.get_roles(user)
    if user != 'Administrator' and 'custom manager' in user_roles:
        
        conditions=""" (`tabCustom Type`.owner = '{user}')""".format(user=user)
        return conditions
    else:
        pass