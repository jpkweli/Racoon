# Racoon

Merging clips in Adobe Premiere causes several problems when trying to export XMLs to color-correct or AAF/OMFs to post-produce sound.
I barely know some programming principles but I've managed to code this App succesfully. Feel free to improve this project!
Racoon imports FCPXMLs made in Adobe Premiere and un-merges clips, Restoring All Clip's Original Names (RACOON).

It operates retrieving all clips' «name», «file_id» and «file > name» attributes. While «name» attribute is stated only the first time a source clip is used, «file_id»s are used to link the subsequent appearances of the same source. RACCON retrieves all clips' id, finds the referring clip «file > name» and replaces «name» tag with the file name. 

Hope you enjoy it and find it usefull :)
