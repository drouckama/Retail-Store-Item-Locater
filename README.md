# Retail-Store-Item-Locater
A device that will scan an item in the store, and return the name of its "home aisle," shelf/row number, and column number. 

Steps to Install:
  1. Install cv2 library
  2. Install pyzbar library
  3. (Longest Part: Contact creator to offer service of creating this file) Create a text file in the same folder titled "planoguide.txt"
          
          
          3a. This Planoguide text file will include the map of your store with this format:
          
         
          3b. 1st column: UPC number, if UPC number string length is greater than 11, cut from the start. Ex: 0073852096521 must change to 73852096521
          3c. 2nd column: column for SKU number (string length does not matter)
          3d. 3rd column: column for shelf number from top to bottom in format "1st", "2nd", "3rd"... ect.
          4d. 4th column: column for column number from left to right in format "1st", "2nd", "3rd"... ect.
          5d. 5th column column for aisle and section number in format aisleName_Section_1...aisleName_Section_2...ect
          
          For example:
          ===         ===       === === =====    =======
          UPC         SKU       Row Col Aisle    Section
          ===         ===       === === =====    =======
          99999999999 676767676 1st 1st aisleName_Section_1
          99999999999 676767676 1st 2nd aisleName_Section_1
          99999999999 676767676 1st 3rd aisleName_Section_1
          99999999999 676767676 1st 4th aisleName_Section_1
          99999999999 676767676 1st 5th aisleName_Section_1
          99999999999 676767676 1st 6th aisleName_Section_1
          99999999999 676767676 1st 7th aisleName_Section_1
          99999999999 676767676 1st 8th aisleName_Section_1
          99999999999 676767676 2nd 1st aisleName_Section_1
          99999999999 676767676 2nd 2nd aisleName_Section_1
          99999999999 676767676 2nd 3rd aisleName_Section_1
          99999999999 676767676 2nd 4th aisleName_Section_1
          99999999999 676767676 2nd 5th aisleName_Section_1
          99999999999 676767676 2nd 6th aisleName_Section_1
          99999999999 676767676 2nd 7th aisleName_Section_1
          99999999999 676767676 2nd 8th aisleName_Section_1
          99999999999 676767676 2nd 9th aisleName_Section_1
          99999999999 676767676 2nd 10th aisleName_Section_1
          99999999999 676767676 3rd 1st aisleName_Section_1
          99999999999 676767676 3rd 2nd aisleName_Section_1
          99999999999 676767676 3rd 3rd aisleName_Section_1
          99999999999 676767676 3rd 4th aisleName_Section_1
          99999999999 676767676 3rd 5th aisleName_Section_1
          99999999999 676767676 4th 1st aisleName_Section_1
          99999999999 676767676 4th 2nd aisleName_Section_1
          99999999999 676767676 4th 3rd aisleName_Section_1
          99999999999 676767676 4th 4th aisleName_Section_1
          99999999999 676767676 4th 5th aisleName_Section_1
          99999999999 676767676 5th 1st aisleName_Section_1
          99999999999 676767676 5th 2nd aisleName_Section_1
          99999999999 676767676 5th 3rd aisleName_Section_1
          99999999999 676767676 5th 4th aisleName_Section_1
          99999999999 676767676 5th 5th aisleName_Section_1
