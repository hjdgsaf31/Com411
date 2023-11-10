
def started(msg=""):
    print("-" * 85)
    print(f"Operation started : {msg}...")


def completed():
    print("\nOperation completed")
    print("-" * 85)


def error(msg):
    print(f"Error!{msg}")


def menu():
    print("\n please select one of the following options: ")
    print(f"{'[years]':<10} List unique years")
    print(f"{'[tally]':>10}Tally up medals")
    print(f"[teams]Tally up medals for each team")
    print(f"[exit]Exit the program")


menu()


def display_team_medal_tally(team_tally):
    print(f"| {'Gold':<10} | {team_tally['Gold']:<10} |")
    print(f"| {'Silver':<10} | {team_tally['Silver']:<10} |")
    print(f"| {'Bronze':<10} | {team_tally['Bronze']:<10} |")


def menu():
    print(f"""Please select one of the following options:
    {"[years]":<10} List unique years
    {"[tally]":<10} Tally up medals
    {"[team]":<10} Tally up medals for each team
    {"[exit]":<10} Exit the program
    """)


#def display_the_years(years):
   # sorted_years = sorted(years, reverse=True)
    #for year in sorted_years:
      #  print(year)











