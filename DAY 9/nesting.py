capitals={
    "France":"Paris",
    "Germany":"Berlin"
}

# Nested list in dictionary

travel_log={
    "France":["Paris","Lille","Dijon"],
    "Germany":["Stuttgart","Berlin"],
}

# accessing "Lille"
print(travel_log["France"][1])

nested_list=["A","B",["C","D"]]

# accessing "D"
print(nested_list[2][1])

travel_log={
    "France":{
        "total_visits":8,
        "cities_visited":["Paris","Lille","Dijon"],
    },
    "Germany":{
        "cities_visited":["Stuttgart","Berlin"],
        "total_visits":5,
    }
}

#accessing "Stuttgart"

print(travel_log["Germany"]["cities_visited"][0])


