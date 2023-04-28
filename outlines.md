jobs app
-categoury
        -name

-company
        -name
        -icon
        -FB link
        -gm-link
        -tw-link
        -yb-link
        -slug

-job
        -auth(relations one to many)
        -title
        -icon
        -location
        -company(relations one to many)
        -categourycompany(relations one to many)
        -job_tybe p&f&r time
        #SUMMARY
        -puplished_at
        -vacancy
        -salary
        -des
        -Responsibilit
        -Qualification
        -Benefits
        -slug

-Candidates
        -job company(relations one to many)
        -name
        -email
        -image
        -linkedin
        -cv
        -cover
        -applied at

settings app
company
        -name
        -slogan
        -logo
        -adress
        -about us
        -aboutus_image
        -our_visin
        -phones
        -emails
        -FB link
        -inst-link
        -tw-link
        -yb-link
        -work_days


        #get in touch forms.form

blog app
-post
        -author
        -title
        -subtitle
        -image
        -puplished at
        -category (relations)
        -artical
        -tag
        -slug

- review
        -post(relations)
        -author(relations)
        -date
        -review

**fake data
** admin customize
account app 
#user login - sighn - up and reset password

#translations

# create api - post man
# debug tool bar

# caching

# debug tool bar
