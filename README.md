# small-bits-of-python
Tree.py prints a tree made of characters. 

*************
idle config files, with color scheme

In debian linux these files are stored in /home/[username]/.idlerc/

If config-highlight.cfg doesn't exist you can add it manually, or from within idle Go to menu Options -> Configure then on the Highlights tab select new theme give it a name (any colors for now, make two themes to better see how they are stored.) save the changes and close Idle. Then find the config file and you can copy and paste this scheme into said file. You can also change the name from " [muhDrk] " to " [anything] " save the file then restart Idle. Go to menu Options -> Configure, Highlights tab, select the custom theme button, and the new theme should be in the dropdown list.

I recomend closing Idle before making external config file changes just so they do not get accidentally over-written.

If you have Idle open when you edit the file Idle will not see the changes until it is restarted. The behavior is to read the config files at startup into a working copy in memory, then when changes made in the configuration-settings dialog are saved it overwrites the original config files with the working copy it has in memory. Idle does not modify single lines within or append lines to the original file. So if Idle is open when you modify an external config file then make a change from within Idle before restarting Idle, the external changes will be lost because Idle doesn't know about them and just writes the working copy to disk.
*************
