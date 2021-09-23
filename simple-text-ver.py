seatList = []
routeList = []
postList = []

print('Mr J Technologies 2021\n')
while True:
    print('-MENU-\n 1. Seats\n 2. Routes\n 3. Reports\n 4. Announcements')
    #wrap
    print(' 5. Stats\n 6. Settings')
    menuItem = input('')
    if menuItem == '1':
        print('-SEATS-\n')
        print(' 1. See Assignments\n 2. Add Student\n 3. Remove Student\n')
        seatsItem = input('')
        if seatsItem == '1':
            print(seatList)
            print('\n')
        if seatsItem == '2':
            addStud = input('Student Name:  ')
            addStudNo = input('Student Seat:  ')
            seatList.append(addStudNo + ': ' + addStud)
            print('Added\n')
        if seatsItem == '3':
            removeList = input('Remove What?\n')
            seatList.remove(removeList)
            print('Removed\n')
            print()
    if menuItem == '2':
        print('-ROUTES-\n')
        print(' 1. See Routes\n 2. Add Route\n 3. Remove Route\n')
        routesItem = input('')
        if routesItem == '1':
            print(routeList)
            print('\n\n')
        if routesItem == '2':
            addRoute = input('Address Name:  ')
            addRouteS = input('Student Name:  ')
            routeList.append(addRouteS + ': ' + addRoute)
            print('Added\n\n')
        if routesItem == '3':
            removeList = input('Remove What?\n')
            routeList.remove(removeList)
    if menuItem == '3':
        print('-REPORTS-\n')
        print(' 1. See Reports\n 2. Delete Reports\n')
        reportsItem = input('')
        if reportsItem == '1':
            print('NO AVAILABLE REPORTS\n') #students can't add
        if reportsItem == '2':
            print('NO REPORTS TO DELETE\n')
    if menuItem == '4':
        print('-ANNOUNCEMENTS-\n')
        print(' 1. New Post\n 2. View Posts\n 3. Delete Posts\n')
        postsItem = input('')
        if postsItem == '1':
            postName = input('Post Name:  ')
            postContent = input('Post Contents:  ')
            postCode = input('Post Code:  ')
            postList.append(postName + ': ' + postContent)
            print('Created\n')
        if postsItem == '2':
            print(postList)
            print()
        if postsItem == '3':
            postList.clear()
            print('Cleared\n')
    if menuItem == '5':
        print('-STATS-\n')
        print(' 1. Bus Hours\n 2. Miles Ridden\n')
        statsItem = input('')
        if statsItem == '1':
            print('NO BUS HOURS\n')
        if statsItem == '2':
            print('NO MILES RIDDEN\n')
    if menuItem == '6':
        print('-SETTINGS-\n')
        print('Settings will be available in next version.\n')



    if menuItem == 'x':
        exit()
