from controller.search_controller import Search_Controller
from controller.user_controller import User_Controller
from model.Shop_model import Shop
from model.User_model import User
from source.Notebooks_DB import Notebooks_DB
from source.User_DB import User_DB


def searching(shop, user):
    end = False
    while not end:
      

        new_search = Search_Controller(shop, user)
        new_search.new_search()

     
        print(new_search.get_user().get_filter())

       
        print("Do you want to make another request?\nInput 'N to stop', Enter to continue")
        n = input()
        if n == 'n' or n == "N":
            end = True


if __name__ == '__main__':
    
    User_DB.init()
    User_Controller.save_user(User("Петя"), User_DB.init())

    my_shop = Shop()
    Shop.set_notebooks(Notebooks_DB.get_notebook_set())

    new_user = User_DB.users.get(0)

    searching(my_shop, new_user)