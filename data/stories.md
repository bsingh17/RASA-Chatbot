

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

## existing customer about product
* about_product
    - utter_ask_current_customer
* yes_customer
    - utter_ask_unique_code
* unique_code
    - action_get_unique_code
* course_selection
    - action_get_course
* payment_confirmation
	- action_payment_confirmed

## new customer, just sales
* about_product
    - utter_ask_current_customer
* no_customer
    - sales_form
    - form{"name":"sales_form"}
* course_selection
	- action_get_course
* payment_confirmation
	- action_payment_confirmed

## new customer, explain person_name
* about_product
    - utter_ask_current_customer
* no_customer
    - sales_form
    - form{"name":"sales_form"}
    - form{"requested_slot":"person_name"}
* explain
    - utter_explain_why_person_name
    - sales_form
    - form{"name":null}


## new customer, explain email
* about_product
    - utter_ask_current_customer
* no_customer
    - sales_form
    - form{"name":"sales_form"}
    - form{"requested_slot":"business_email"}
* explain
    - utter_explain_why_email
    - sales_form
    - form{"name":null}


## new customer, explain city
* about_product
    - utter_ask_current_customer
* no_customer
    - sales_form
    - form{"name":"sales_form"}
    - form{"requested_slot":"city"}
* explain
    - utter_explain_why_city
    - sales_form
    - form{"name":null}


## new customer, explain phone_number
* about_product
    - utter_ask_current_customer
* no_customer
    - sales_form
    - form{"name":"sales_form"}
    - form{"requested_slot":"phone_number"}
* explain
    - utter_explain_why_phone_number
    - sales_form
    - form{"name":null}

## contact sales and take course
* contact_sales
	- sales_form
	- form{"name":"sales_form"}
* course_selection
	- action_get_course
* payment_confirmation
	- action_payment_confirmed
	
## just sales, continue
* contact_sales
    - sales_form
    - form{"name": "sales_form"}
* faq
    - respond_faq
    - sales_form
    - form{"name": null}

## explain person name
* contact_sales
    - sales_form
    - form{"name": "sales_form"}
    - slot{"requested_slot": "person_name"}
* explain
    - utter_explain_why_person_name
    - sales_form
    - form{"name":null}

## explain business email
* contact_sales
    - sales_form
    - form{"name":"sales_form"}
    - slot{"requested_slot": "business_email"}
* explain
    - utter_explain_why_email
    - sales_form
    - form{"name":null}

## explain city
* contact_sales
    - sales_form
    - form{"name": "sales_form"}
    - slot{"requested_slot": "city"}
* explain
    - utter_explain_why_city
    - sales_form
    - form{"name":null}

## explain phone_number
* contact_sales
    - sales_form
    - form{"name" : "sales_form"}
    - slot{"requested_slot": "phone_number"}
* explain
    - utter_explain_why_phone_number
    - sales_form
    - form{"name":null}




