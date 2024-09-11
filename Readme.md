## Steps to develop add-ons on vscode and blender

- Open `Vs Code`
- Activate this extension
  https://marketplace.visualstudio.com/items?itemName=JacquesLucke.blender-development
- Open the folder in the `VS code`
- Press `ctrl+shift+p` to open the `Command Palette`, Search for `New Addon` then select `Simple`
  It will ask for a name for the add-ons, Developer Name, Support for the previous Blender Version & the folder where the development file will be added

  Finally, it will generate 2 files, required for a simple blender addon.

- Open `Command Palette` again with `ctrl+shift+p` and this time search for `Blender Start`
  This will ask you to select the specific version of Blender where you want to install the `addon`
  Next, the Blender version should open automatically, go to `Preferences`> `Add-ons` > Search for `[Your Add-ons Name]`  
   Open `Command Palette` again with `ctrl+shift+p` and this time search for `Blender Start`
  This will ask you to select the specific version of Blender where you want to install the `addon`
  Next, the Blender version should open automatically, go to `Preferences`> `Add-ons` > Search for `[Your Add-ons Name]`

  At this moment nothing special happened, we have just registered the add-ons

- Press `ctrl+shift+p` to open the `Command Palette`, Search for `Select Interpreter`
  Select the Windows version of Python, usually located inside the `c` drive
  Then open Windows `Terminal` with the `Run as Administrator` privilege
- Install this package
  Import blender package using

  ```bash
  import bpy
  ```

  If you see this type of error

  ```bash
  pip install fake-bpy-module
  ```

  From this url https://github.com/nutti/fake-bpy-module
  This will fake the `bpy` (Blender Python Package) module

- Open command palette and run `Blender: Reload Addon` to reflect the updated code in blender

## Steal template code from blender

In scripting viewer on blender there is a menu item called `Templates`. This contains the basic blueprint code for `operator`, `ui panel` etc.
