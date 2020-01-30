from datetime import datetime

from flask import render_template, request, redirect, url_for, flash

from app import app, db
from app.models import WayfairManualProcesseds

@app.route('/', methods=["GET", "POST"])
@app.route('/index',methods=["GET", "POST"])
def index():

    if request.form:
        PurchaseOrderNumber = request.form.get('ep')
        Created_At = datetime.now()

        po = WayfairManualProcesseds(PurchaseOrderNumber,Created_At)
        db.session.add(po)
        db.session.commit()

    all_po = WayfairManualProcesseds.query.all()

    return render_template('index.html', pos=all_po)


@app.route('/delete/<id>/', methods=['GET', 'POST'])
def delete(id):
    my_data = WayfairManualProcesseds.query.get(id)
    db.session.delete(my_data)
    db.session.commit()
    flash("PO Mapping Deleted Successfully")

    return redirect(url_for('index'))


@app.route('/insert', methods=['POST'])
def insert():
    if request.method == 'POST':
        PurchaseOrderNumber = request.form.get('ep')
        Created_At = datetime.now()

        po = WayfairManualProcesseds(PurchaseOrderNumber, Created_At)
        db.session.add(po)
        db.session.commit()

        flash("PO Inserted Successfully")

        return redirect(url_for('index'))

@app.route('/update', methods=['GET', 'POST'])
def update():

    if request.method == 'POST':
        my_data = WayfairManualProcesseds.query.get(request.form.get('id'))

        my_data.PurchaseOrderNumber = request.form.get('ep')
        my_data.Updated_At = datetime.now()

        db.session.commit()
        flash("PO Updated Successfully")

        return redirect(url_for('index'))
