# Project for handling files and folders

from pathlib import Path
import shutil

# Defining a function which return paths
def get_path() :
    name = input("Enter the File/Folder name : ")
    return Path(name)

# Defining a function to create a folder
def create_folder() :
    try : 
        path = get_path()
        path.mkdir()
            
    except Exception as error :
        print(f"Sorry Got Some Error : {error}")    
    

# Defining method to read files and folders
def read_files_folders() :
        path = Path.cwd()
        items = list(path.iterdir())
        
        # Displaying the files and folders
        print("----------------")
        for i, v in enumerate(items) :
            print(f"{i + 1} : {v}")     
        print("----------------")
        

# Defining method to update the folders
def update_folder() :
    # List out the files and folders
    read_files_folders()
    
    try : 
        # Taking the name of the folder from the usesr 
        path = get_path()
    
        # Check whether the folder name is in existance or not
        if path.exists() and path.is_dir() :
            new_path = get_path()
            path.rename(new_path)
            print(f"{path.name} to {new_path.name} Renamed Successfull!")
        else :
            print(f"Folder Does Not Exist!")
            
    except Exception as error :
        print(f"Sorry Got Some Error : {error}")  
      
        
# Defining method to delete the folders
def delete_folder() :
    # List out the files and folders
    read_files_folders()
     
    try : 
        # Taking the name of the folder from the user
        path = get_path()
        
        # Check whether the folder name is in existance or not
        if path.exists() and path.is_dir() :
            shutil.rmtree(path)
            print(f"{path.name} deleted successfully!")
        else :
            print(f"Sorry this folder doesn't exists!")
            
    except Exception as error :
        print(f"Sorry Got Some Error : {error}")           
  
  
# Defining method to create a file 
def create_file() :
    
    # List out the files and folders
    read_files_folders()
    
    try :
        # Taking the file name from the user
        path = get_path()
        
        # Check whether the folder name is in existance or not 
        if not path.exists() :
            with open(path, "w") as fs :
                data = input("Enter content : ")
                fs.write(data)
                print(f"{path} File Created Successfully!")
        else :
            print(f"File Already Exists!")
            
    except Exception as error :
        print(f"Sorry Got Some Error : {error}")     
        

# Defining a method to read a file
def read_file() :
    # List out the files and folders
    read_files_folders()
    
    try :
        # Taking the file name from the user 
        path = get_path()
        
        # Check whether the file is in existance or not
        if path.exists() and path.is_file() :
            with open(path, "r") as fs :
                data = fs.read()
                print(data)
        else :
            print(f"File Does not exist!")
                
    except Exception as error :
        print(f"Sorry Got Some Error : {error}")     
         
# Defining a function to update a file 
def update_file():
    # List out the files and folders
    read_files_folders()
    
    # Taking the file name from the user 
    path = get_path()
    
    try : 
        # Check whether the file is in existance or not 
        if path.exists() and path.is_file() :
            print("\n-------------")
            print(f"1. Rename file ")
            print(f"2. Add content to the file ")
            print(f"3. Rewrite file ")
            print("-------------")
            
            # Taking the choice from the user 
            ch = int(input("Enter the choice : "))
            
            if ch == 1 :
                # Taking the new name for the file from the user   
                new_path = get_path()
                if not new_path.exists() :
                    path.rename(new_path)
                    print(f"{path.name} to {new_path.name} renamed successully!")
                else :
                    print(f"OOPS {new_path} already exist!")
                    
            elif ch == 2 :
                # Opening the file to add content to the file
                with open(path, "a") as fs:
                    content = input("Enter the content : ")
                    fs.write(" " + content)
                    print(f"Content Added Sucessfully!")
                    
            elif ch == 3:
                # Opening the file to rewrite the file
                with open(path, "w") as fs:
                    content = input("Enter the content : ")
                    fs.write(content)
                    print(f"Rewritten Done Successfully!")
        else :
            print(f"File Does Not Exist!")
                
    except Exception as error :
        print(f"Sorry Got Some Error : {error}")   
        
# Defining a method to delete a file 
def delete_file():
    # List out the files and folders
    read_files_folders()
    
     # Taking the name of the file to delete
    path = get_path()
    
    try :
        # Check whether the file is in existance or not 
        if path.exists() and path.is_file() :
            path.unlink()
            print(f"{path.name} file deleted successfully!")
        else :
            print(f"OOPS {path.name} file doesn't exists!")
            
    except Exception as error :
        print(f"Sorry Got Some Error : {error}")  


# While loop to iterate it until user enter 0
while True :
    # Providing choices 
    print("\n======= File & Folder Management =======")
    print("1. Create a Folder ")
    print("2. Read Files and Folders ")
    print("3. Update the folder ")
    print("4. Delete the folder ")
    print("5. Create a file ")
    print("6. Read a file ")
    print("7. Update a file ")
    print("8. Delete a file ")
    print("0. Exit ")
    print("========================================")
    
    try :
        # Taking choice from the user 
        choice = int(input("Enter your choice : "))
        if choice == 1 :
            create_folder()
        elif choice == 2:
            read_files_folders()
        elif choice == 3:
            update_folder()
        elif choice == 4 :
            delete_folder()
        elif choice == 5:
            create_file()
        elif choice == 6:
            read_file()
        elif choice == 7:
            update_file()  
        elif choice == 8:
            delete_file()     
        elif choice == 0:
            break
        else :
            print(f"{choice} is wrong! Please try again!")
    
    except Exception as error :
        print(f"Sorry Got Some Error : {error}")  