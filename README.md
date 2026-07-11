# PawnbrokerInventory
# Chit Fund Application

A desktop-based Chit Fund / Pawnbroker Inventory Management application developed using **Python** and **SQLite**.

## Technology Stack

- Python 3.x
- SQLite
- Tkinter
- tkcalendar

---

## Project Structure

```
ChitFund/
│
├── main.py
├── config.py
├── database.py
│
├── database/
│   └── ChitFundApplication.db
│
├── modules/
│   ├── signin.py
│   ├── dashboard.py
│   ├── open_chit.py
│   ├── close_chit.py
│   ├── reports.py
│   ├── search.py
│   ├── customer.py
│   ├── settings.py
│   └── start_new_record.py
│
├── services/
│   ├── chit_service.py
│   ├── customer_service.py
│   ├── report_service.py
│   ├── settings_service.py
│   └── record_service.py
│
├── database/
│   └── ChitFundApplication.db
│
├── backup/
│
├── reports/
│
└── assets/
    ├── banner.png
    ├── icons/
    └── images/
```

---

## Database Tables

### Entries

| Column | Type |
|---------|------|
| Date | DATE |
| CustName | VARCHAR |
| ChitNo | VARCHAR |
| Info | VARCHAR |
| Weight | VARCHAR |
| Status | INTEGER |
| Months | INTEGER |
| Principal | REAL |
| InAmt | REAL |
| InterAmt | REAL |
| OutAmt | REAL |
| Total | REAL |

### Available

| Column | Type |
|---------|------|
| ChitNo | VARCHAR |
| Info | VARCHAR |
| Weight | VARCHAR |

### Customer

| Column | Type |
|---------|------|
| CID | VARCHAR |
| CName | VARCHAR |

---

## Modules

### Sign In

- Username authentication
- Password authentication
- Opens Dashboard after successful login

---

### Dashboard

- Open a Chit
- Close a Chit
- Generate Report
- Start New Record
- General Settings
- Add Customer
- Search

---

### Open a Chit

- Select customer
- Add customer shortcut
- Enter item description
- Enter weight
- Enter amount
- Creates new chit
- Updates inventory
- Updates running balance

---

### Close a Chit

- Displays active chits
- Calculates month difference
- Calculates payable amount
- Removes inventory
- Updates running balance

---

### Generate Report

- Select start date
- Select end date
- Export CSV report

---

### Start New Record

- Check current balance
- Backup SQLite database
- Backup Entries table as CSV
- Delete closed records
- Insert "New FY Balance" entry

---

### General Settings

- Modify Interest %
- Modify Chit Start
- Modify Chit End

---

### Customer

- Add Customer ID
- Add Customer Name

---

### Search

- Search customer
- Display customer transaction history

---

## Backup

Database backups are stored inside

```
backup/<PreviousYear>_<CurrentYear>/
```

Contents

```
ChitFundApplication.db
backup.csv
```

---

## Reports

Reports are generated inside

```
reports/
```

Format

```
<StartDate>_to_<EndDate>.csv
```

---

## Running the Application

```bash
python main.py
```

---

## Required Package

```bash
pip install tkcalendar
```

---

## Default Login

Username

```
admin
```

Password

```
admin
```

---

## Developed Using

- Python
- SQLite
- Tkinter
- tkcalendar