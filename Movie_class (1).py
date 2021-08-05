class Movie:
    def __init__(self,name,genre,director,cast,year,summary=''): # constructer
        self.name=name
        self.genre=genre
        self.director=director
        self.year=year
        self.summary=summary
        self.cast=cast
    def details(self):
        print("Name of movie: ",self.name)
        print("Cast of movie: ",self.cast)
        print("Director of movie: ",self.director)
        print("Year of movie: ",self.year)
        
        
    def addsactmember(self,cas):

        f=self.cast
        f=str(f)+','+str(cas)  # first convert 'cas' into string an then add it to already string 'f' of cast names and then update it.
        self.cast=f
    def change_direc(self,name):
        self.director=name
    def addsummary(self,summary):
        self.summary=summary
    def viewsummary(self):
        return self.summary
    
if __name__ == "__main__":
    t=Movie("mohan","historical","haegde","A",2016,"this is summary")
    p=1
    t.addsactmember(" B")
    t.addsactmember(" C")
    t.addsactmember(" D")
    t.addsummary("this gonna be long so skipped it")
    t.details() # to print all the details before changing director
    print('*'*20)
    t.addsactmember(" E")
    print(t.viewsummary())
    t.change_direc("Hypocrite")   
    t.details()   # to print details after changing the director


   
# variables-name,genre,cast,director,years
# functions - details,addsactmember(name),changedirector(name),addsummary(summary),viewsummary()