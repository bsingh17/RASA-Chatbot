

## thank
* thank
  - utter_noworries

## goodbye
* bye
  - utter_bye

## Some question from FAQ
* faq
    - respond_faq

## sales form
* contact_sales
    - sales_form
    - form{"name": "sales_form"}
    - form{"name": null}

## just sales, continue
* contact_sales
    - sales_form
    - form{"name": "sales_form"}
* faq
    - respond_faq
    - sales_form
    - form{"name": null}

## explain email
* contact_sales
    - sales_form
    - form{"name": "sales_form"}
    - slot{"requested_slot": "business_email"}

## explain budget
* contact_sales
    - sales_form
    - form{"name":"sales_form"}
    - slot{"requested_slot": "budget"}

## explain company
* contact_sales
    - sales_form
    - form{"name": "sales_form"}
    - slot{"requested_slot": "company"}

## explain person_name
* contact_sales
    - sales_form
    - form{"name" : "sales_form"}
    - slot{"requested_slot": "person_name"}

## explain use_case
* contact_sales
    - sales_form
    - form{"name" : "sales_form"}
    - slot{"requested_slot": "use_case"}

## explain job_function
* contact_sales
    - sales_form
    - form{"name": "sales_form"}
    - slot{"requested_slot": "job_function"}

