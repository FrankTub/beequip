## Introduction
In this repository we explore a new REST-API for beequip.

## Contributors
- [Frank Tubbing](https://tsgit.transfer-solutions.com/frank_tubbing)

## Approach
Download latest [anaconda version](https://docs.anaconda.com/anaconda/install/windows/) and install this.

Open anaconda prompt and run.
 
``` bash
conda install -c anaconda flask
conda install pandas
conda install -c conda-forge flask-restful
conda install numpy
conda update --all
conda uninstall numpy
conda install numpy
conda install -c anaconda mkl-service
conda install pandas
conda install -c anaconda sqlite
conda install -c anaconda sqlalchemy
conda install -c conda-forge flask-sqlalchemy
```

Found out later that debugging in vsc resulted in error due to missing the conda location in `PATH` windows variable. Add following paths:
```bash
%USERPROFILE%\Anaconda3\Library\bin
%USERPROFILE%\Anaconda3\Scripts
%USERPROFILE%\Anaconda3\condabin
%USERPROFILE%\Anaconda3
```

Download [sqlite](https://www.sqlite.org/download.html) and use precompiled Binaries for Windows. Open command prompt and navigate to location where you placed the sqlite binaries, in my case `C:\Program Files\Sqlite` and create a database file in this repo.  Edit: could also have used following [approach](https://flask.palletsprojects.com/en/2.0.x/tutorial/database/).

```bash
cd "C:\Program Files\Sqlite"
sqlite3
.open 'C:\Users\frank_tubbing\source\repos\beequip\beequip.db'
```

Now create the following tables, with sql snippet.
```sql
drop table if exists customers;
drop table if exists installments;
drop table if exists leases;
create table customers(id int, coc_number varchar(30), name varchar(50));
create table installments(installment_no varchar(30), t id, date text, installment double, principal double, interest double, outstanding_start double);
create table leases(id int, customer_id int, reference varchar(30), installment_no varchar(30), lane varchar(30), team varchar(30), object_brand varchar(30), object_type varchar(50));
```


Download [SQLiteStudio](https://sqlitestudio.pl/), import all csv's into the database with the gui. Make sure to mark `First line represents CSV column names`. Verify that the data is in the database with sql statements like.
```sql
select * from customers;
select * from leases;
select * from installments;
```

## Results
- What's the outstanding for a lease given a reference and date?
```sql
select outstanding_start -- not sure if required to aggregrate it
from   leases lss join installments ism on lss.installment_no = ism.installment_no
where  lss.reference = 'BQ2333.20132.01'
and    date(ism.date) = date('2017-12-05')
```

This can be achieved by our app by running `app.py`. I did this using visual studio code and run app.py. Output is something like.
```text
 * Serving Flask app "app" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```
Use the url that is provided and add the following `outstandingleaseamount?reference=BQ2333.20132.01&date=2017-12-05`, in my example this will look like `http://127.0.0.1:5000/outstandingleaseamount?reference=BQ2333.20132.01&date=2017-12-05`. Note that the date should always be formatted in `YYYY-MM-DD`.

- What's the total outstanding for a organisation given a Camber of Commerce number and date?
```sql
select sum(outstanding_start) as outstanding_start -- not sure if required to aggregrate it
from   leases lss 
join   installments ism on lss.installment_no = ism.installment_no
join   customers ctm on lss.customer_id = ctm.id
where  ctm.coc_number = '32076937'
and    date(ism.date) = date('2017-12-05' )
```
- What's the total outstanding per team and lane given a date?
```sql
select lss.lane, lss.team, sum(outstanding_start)
from   leases lss join installments ism on lss.installment_no = ism.installment_no
where  1=1
and    date(ism.date) = date('2017-12-05')
group by lss.lane, lss.team
```
- What's the average outstanding at the start of the lease per team and lane?
```sql
select lss.lane, lss.team, avg(outstanding_start)
from   leases lss join installments ism on lss.installment_no = ism.installment_no
where  ism.t = 1
group by lss.lane, lss.team
```
- What's the total daily outstanding given a year?
==> Note sure what your definition is.

## File descriptions
Within the repo you'll find the following directorie(s) and file(s_).

```text
beequip/
├── app.py # main python file to start the api
├── model.py # database structure declared
├── beequip.db # SQLite database containing original csv data
├── README.md
└── data/
    ├── customers.csv
    ├── installments.csv 
    └── leases.csv 
```