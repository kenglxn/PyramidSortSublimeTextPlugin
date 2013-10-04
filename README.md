PyramidSortSublimeTextPlugin
============================

Sorts selected text based on line length, from shortest to longest, while cutting out empty lines

So this:

    foobar
    bazolino
    
    barolainen
    foo

Becomes:
    
    foo
    foobar
    bazolino
    barolainen

# Installing using [Package Control](http://wbond.net/sublime\_packages/package\_control)

* Start Command Palette (Command+Shift+p).
* Select "Package Control: Install Package"
* Select PyramidSort when the list appears.

# Installing from command line

Simply clone this repository into the Packages folder of sublime. E.g:
    
    cd ~/Library/Application\ Support/Sublime\ Text\ 2/Packages/
    git clone https://github.com/kenglxn/PyramidSortSublimeTextPlugin.git
