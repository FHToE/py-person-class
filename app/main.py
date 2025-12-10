from __future__ import annotations


class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.people[name] = self


def create_person_list(people: list) -> list:
    created_people = [
        Person(
            name=person["name"],
            age=person["age"],
        )
        for person in people
    ]

    if not created_people:
        return []

    all_created_people = created_people[0].people

    for person in people:
        if "wife" in person and person["wife"] is not None:
            person_instance = all_created_people[person["name"]]
            wife_instance = all_created_people[person["wife"]]
            person_instance.wife = wife_instance

        if "husband" in person and person["husband"] is not None:
            person_instance = all_created_people[person["name"]]
            husband_instance = all_created_people[person["husband"]]
            person_instance.husband = husband_instance

    return created_people
