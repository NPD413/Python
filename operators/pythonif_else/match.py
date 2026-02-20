"""istead of writing many if else statements we can use the match statement the match statement selects one of many code blocks to be executed"""
day=4
match day:
    case 1:
        print("mon")
    case 2:
        print("tue")
    case 3:
        print("wed")
    case 4:
        print("thurs")
    case 5:
        print("fri")

month=5
day=5
match day:
    case 1 |2|3|4|5 if month==4:
        print("a weekend in april")
    case 1|2|3|4|5 if month ==5:
        print("may")
    case _:
        print("no match")