MakerBot Unicorn G-Code Output for Inkscape
===========================================

Notice
------

**This extension is no longer supported or maintained. The last tested version of Inkscape is 0.48.5.**

**Please feel free to fork and improve this extension for your own needs!**

This is an Inkscape extension that allows you to save your Inkscape drawings as
G-Code files suitable for plotting with the [MakerBot Unicorn Pen Plotter](http://store.makerbot.com/makerbot-unicorn-pen-plotter-kit.html).

**Users who use this extension to generate G-Code for a machine other than a MakerBot CupCake CNC with a Unicorn Pen Plotter attachment do so at their own risk.**

Author: [Marty McGuire](http://github.com/martymcguire)

Website: [http://github.com/martymcguire/inkscape-unicorn](http://github.com/martymcguire/inkscape-unicorn)

Credits
=======

* Marty McGuire pulled this all together into an Inkscape extension.
* [Inkscape](http://www.inkscape.org/) is an awesome open source vector graphics app.
* [Scribbles](https://github.com/makerbot/Makerbot/tree/master/Unicorn/Scribbles%20Scripts) is the original DXF-to-Unicorn Python script.
* [The Egg-Bot Driver for Inkscape](http://code.google.com/p/eggbotcode/) provided inspiration and good examples for working with Inkscape's extensions API.

Install
=======

Copy the contents of `src/` to your Inkscape `extensions/` folder.

Typical locations include:

* OS X - `/Applications/Inkscape.app/Contents/Resources/extensions`
* Linux - `/usr/share/inkscape/extensions`
* Windows - `C:\Program Files\Inkscape\share\extensions`

Usage
=====

* Size and locate your image appropriately:
	* The CupCake CNC build platform size is 100mm x 100mm.
	* Setting units to **mm** in Inkscape makes it easy to size your drawing.
	* The extension will automatically attempt to center everything.
* Convert all text to paths:
	* Select all text objects.
	* Choose **Path | Object to Path**.
* Save as G-Code:
	* **File | Save a Copy**.
	* Select **MakerBot Unicorn G-Code (\*.gcode)**.
	* Save your file.
* Preview
	* For OS X, [Pleasant3D](http://www.pleasantsoftware.com/developer/pleasant3d/index.shtml) is great for this.
	* For other operating systems... I don't know!
* Print!
	* Open your `.gcode` file in [ReplicatorG](http://replicat.org/)
	* Set up your Unicorn and pen.
	* Center your build platform.
	* Click the **Build** button!

TODOs
=====

* Rename `*PolyLine` stuff to `*Path` to be less misleading.
* Formalize "home" to be a reasonable place to change pages/pens.
* Parameterize smoothness for curve approximation.
* Use native curve G-Codes instead of converting to paths?
* Include example templates?
