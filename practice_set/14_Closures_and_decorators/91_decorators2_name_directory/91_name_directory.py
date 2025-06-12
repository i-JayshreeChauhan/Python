
def person_lister(f):
    def inner(people):
        #here i need to sort people list according to their age
        """
        PEOPLE = [
                    ['Mike', 'Thomson', '20', 'M'],
                    ['Robert', 'Bustle', '32', 'M'],
                    ['Andria', 'Bustle', '30', 'F']
                 ]
        """
        people.sort(key=lambda person: int(person[2]))
        return [f(p) for p in people]  # Collect and return results
        
        
    return inner

@person_lister
def name_format(person):
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]

if __name__ == '__main__':
    people = [input().split() for i in range(int(input()))]
    print(*name_format(people), sep='\n')