from py.thrift.generated.ttypes import Person


class PersonServiceImpl:

    def getPersonByUsername(self, username):
        print("------getPersonByUsername-----------" + username)
        person = Person()
        person.username = username
        person.age = 20
        person.married = False
        return person

    def savePerson(self, person):
        print(" go to client params ")
        print(person.username)
        print(person.age)
        print(person.married)
