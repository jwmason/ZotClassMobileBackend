import json

def dict(dict1):
    school_list = dict1["schools"]
    first_department = school_list[0]
    all_departments = first_department["departments"]
    course_list = all_departments[0]
    grab_course = course_list["courses"]
    main_list = []
    for course in grab_course:
        var_title = course['courseTitle']
        list1 = []
        grab_sections = course["sections"]
        for section in grab_sections:
            var_seccode = section['sectionCode']
            var_units = section['units']
            var_instructor = section['instructors']
            grab_meetings = section['meetings']
            list3 = []
            for meeting in grab_meetings:
                var_days = meeting['days']
                var_time = meeting['time']
                dict3 = {'days': var_days, 'time': var_time}
                list3.append(dict3)
            section_dict = {"sectionCode": var_seccode, "units": var_units, "instructors": var_instructor}
            list1.append(section_dict)
        dict2 = {'courseTitle': var_title, 'sections': list1, 'meetings': list3}
        main_list.append(dict2)
    print(main_list)
