# UpNote MarkDown Export: Categories to Folder Structure

### A python script to preserve folder structure for UpNote markdown exports. 

This allows you to use your exports in other programs such as Joplin and maintain your notebook/folder structure.
 
There is a version of the script that keeps the categories header UpNote adds, and the other removes it.

## Important
 ***This only works fully if each note is in one category/notebook** (though you can make it work otherwise.)*
 
Notes will only be moved to folders for the **first** listed category. 
* Any other categories/note locations will not have folders created.
* This avoids multiple copies of the same document being created, as updates would not sync.

Category header removal simply takes out the first four lines of each file with categories.
* Files with separate categories will have parts of the header leftover.
* For this case, it is recommended to use the option that retains the header.

This script is simple and works for my use case of each note existing in one location in UpNote. 

## Details
* Python script works nearly instantly.
* Doesn't alter your documents. 
  * Category header removal restores your documents to their imported state.
  * Ability to maintain the added category header if desired
* Runs in the source directory, no code configuration needed.
* Works by parsing the third line of each .md file which contains the categories folder structure.

## Prerequisites
* Python: https://www.python.org/downloads/
* UpNote Premium (for exporting ability): https://getupnote.com/#pricing
  * Currently only the Windows version has the export feature, but the script works on Mac :)
 
## Instructions
1. Export your UpNote notebooks as markdown (premium is required).
   * Settings > General > Export all notes > Export as Markdown
2. Open the directory and place the script inside.
3. Right click the file and Open With... Python (Windows) or Python Launcher (Mac).
   * <code>FolderStruct.py</code> removes the added category headers. <code>FolderStruct+KeepHeaders.py</code> keeps these headers.

And that's it! The script will create the respective folders and sort the files into them. 

The media remains in the initial Files folder.

Any templates and notes that are not categorized will be moved into the Uncategorized folder.

You can delete the script from the folder or save it elsewhere for later use.
