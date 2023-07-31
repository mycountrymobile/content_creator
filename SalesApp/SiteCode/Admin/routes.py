from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_required, current_user
from pandas import read_excel
from SiteCode.models import SalesPerson

admin = Blueprint("admin", __name__)

original_data = read_excel(r'SiteCode/Live Data/vendor.xlsx')
original_data = original_data[original_data["Cost"] > 0]
original_data2 = read_excel(r'SiteCode/Live Data/customer.xlsx')
original_data2 = original_data2[original_data2["Revenue"] > 0]
data = None
data2 = None
active = "All"
active2 = "All"


@admin.route('/setup')
@login_required
def setup():
    global original_data2, original_data, active, active2, data, data2
    active, active2 = "All", "All"
    data, data2 = None, None
    comp = set(current_user.companies_available.split(','))
    original_data = original_data[original_data['Carrier'].isin(comp)]

    original_data2 = original_data2 if current_user.username == "Admin1" else \
        original_data2[original_data2['Carrier'].str.contains('|'.join(comp), case=False)]

    return redirect(url_for('admin.partner_admin'))



@login_required
@admin.route('/partneradmincustomer')
def customer_table():
    comp = SalesPerson.query.filter_by(username=current_user.username)
    comp = comp.first().companies_available.split(',')
    data = original_data2 if data2 is None else data2
    colour = "danger" if current_user.entity in ["Acepeak", "TechOpen", "Letsdial", "Teloz", "Rosper"] else "primary"
    return render_template('partneradmincustomer.html', companies_available=comp, active=active2, data=data,
                           headings=["Carrier", "Country", "Revenue"], colour=colour)


@admin.route('/processtablecustomer/<string:company>')
def process_table_customer(company):
    global original_data2, data2, active2
    if company != "All":
        active2 = company
        data2 = original_data2[original_data2['Carrier'].str.lower().str.contains(company.lower())]
    else:
        data2 = None
        active2 = "All"
    return redirect(url_for('admin.customer_table'))



@login_required
@admin.route('/processtable/<string:company>')
def process_table(company):
    global original_data, data, active
    if company != "All":
        active = company
        data = original_data[original_data['Cost'] > 0]
        data = data[data['Carrier'] == company]
    else:
        data = None
        active = "All"
    return redirect(url_for("admin.partner_admin"))


@admin.route('/partneradmin')
@login_required
def partner_admin():
    global original_data, data, active
    if current_user.role != 2:
        return redirect(url_for('main.home'))
    comp = SalesPerson.query.filter_by(username=current_user.username)
    comp = comp.first().companies_available.split(',')
    table = data if data is not None else original_data
    colour = "danger" if current_user.entity in ["Acepeak", "TechOpen", "Letsdial", "Teloz", "Rosper"] else "primary"
    return render_template('partner_admin.html', companies_available=comp, headers=["Carrier", "Country", "Cost"],
                           data=table, active=active, colour=colour)
