# -*- coding: utf-8 -*-
#
# Modified June-2022 for more recent version of sphinx
#
# OSGeoLive documentation build configuration file, created by
# sphinx-quickstart on Wed Sep 22 19:00:58 2010.
#
# This file is execfile()d with the current directory set to its containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.
#
# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the options.
# For a full list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import sys, os

iso_size = @iso_size@
vm_7z_size = @vm_7z_size@
req_hd_size = @req_hd_size@

# -- Project information -----------------------------------------------------

project = u'@OSGeoLiveDoc_NAME@'
copyright = u'2011~2022, OSGeo'
version = '@OSGeoLiveDoc_VERSION_MAJOR@.@OSGeoLiveDoc_VERSION_MINOR@'
release = '@OSGeoLiveDoc_VERSION_MAJOR@.@OSGeoLiveDoc_VERSION_MINOR@'

# -- General configuration -----------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be extensions
# coming with Sphinx (named 'sphinx.ext.*') or your custom ones.
extensions = [ ]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of directories, relative to source directory, that shouldn't be searched
# for source files.
exclude_trees = [ ]
exclude_patterns = [ ]

# The suffix of source filenames.
source_suffix = '.rst'

# The encoding of source files.
#source_encoding = 'utf-8-sig'

# The master toctree document.
root_doc = 'index'

# today_fmt is used as the format for a strftime call.
today_fmt = '%B %d, %Y'

# -- Options for internationalization -----------------------------------------

# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = 'en'

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
#show_authors = True

# The name of the Pygments (syntax highlighting) style to use.
#pygments_style = 'sphinx'


# -- Options for HTML output ---------------------------------------------------

# The theme to use for HTML and HTML Help pages.  Major themes that come with
# Sphinx are currently 'default' and 'sphinxdoc'.
html_theme = 'overview'
html_theme_path = ['_themes']

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
#html_title ='|project| |release| documentation'
html_title='%(projectname)s %(projectversion)s Documentation' % { 'projectname':project,'projectversion': release }

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
html_static_path = ['@CMAKE_CURRENT_SOURCE_DIR@/_static']
html_favicon = '@CMAKE_CURRENT_SOURCE_DIR@/_static/favicon.ico'

html_css_files = [
    '../_themes/overview/static/overview.css',
]

html_copy_source = False

html_last_updated_fmt = '%b %d, %Y'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
#html_use_smartypants = True

# Additional templates that should be rendered to pages, maps page names to
# template names.
#html_additional_pages = {}

# If false, no module index is generated.
#html_use_modindex = True

# If false, no index is generated.
#html_use_index = True

# If true, the index is split into individual pages for each letter.
#html_split_index = False

# If true, links to the reST sources are added to the pages.
#html_show_sourcelink = True

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
#html_use_opensearch = ''

# If nonempty, this is the file name suffix for HTML files (e.g. ".xhtml").
#html_file_suffix = ''

# Output file base name for HTML help builder.
htmlhelp_basename = '%sdoc' % project


# -- Options for locale output --------------------------------------------------
locale_dirs = ['@CMAKE_SOURCE_DIR@/locale']   # path is example but recommended.
gettext_compact = False     # optional.
gettext_auto_build = True

# -- Options for LaTeX output --------------------------------------------------

latex_elements = {
# The paper size ('letterpaper' or 'a4paper').
'papersize': 'a4paper',

# The font size ('10pt', '11pt' or '12pt').
'pointsize': '10pt',

# remove blank pages
'classoptions': ',oneside',
'babel': '\\usepackage[english]{babel}'

# Additional stuff for the LaTeX preamble.
#'preamble': ''
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author, documentclass [howto/manual]).
latex_documents = [
  ('index', 'OSGeoLive.tex', u'OSGeoLive Documentation',
   u'OSGeo', 'manual'),
]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
#latex_logo = None

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
#latex_use_parts = False

# If true, show page references after internal links.
#latex_show_pagerefs = False

# If true, show URL addresses after external links.
#latex_show_urls = False

# Documents to append as an appendix to all manuals.
#latex_appendices = []

# If false, no module index is generated.
#latex_domain_indices = True

# Linkcheck configuration, see http://sphinx.pocoo.org/latest/config.html#options-for-the-linkcheck-builder

linkcheck_retries = 3  # default is 1

# About User-Agent:
# https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/User-Agent
linkcheck_request_headers = {
    "*": { 'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:25.0) Gecko/20100101 Firefox/25.0' },
}

linkcheck_ignore = [
        # currently SSL_ERROR_BAD_CERT_DOMAIN
        # TODO remove this line when the CERT is fixed
        r'https://www.rspatial.org',


        # NewConnectionError looks like information is wrong
        r'http://udig.refractions.net',

        # link exists but does not accept robots and linkchecker is a robot
        # used in overview/mapserver_overview
        'http://www.dnr.state.mn.us/maps/compass.html',

        # intermittent 502 server errors
        r'https://demo.pycsw.org',

        # TODO this link is failing: RemoteDisconnected('Remote end closed connection without response'))
        # ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))
        'https://www.iso.org',
        r'https://inspire.ec.europa.eu',

        # HTTPSConnectionPool
        r'https://worldwind.arc.nasa.gov/java/',
        r'https://r-spatial.org',

        # links to the disk internals
        r'http://localhost', r'https://localhost',
        r'http://127.0.0.1', r'https://127.0.0.1',
        r'http://0.0.0.0',
        'http://geonode',

        # links to old versions
        r'https://live.osgeo.org/archive/15.0',
        r'https://live.osgeo.org/archive/16.0',

        # For the following an appropiate user agent is needed
        # 403 Client Error
        r'https://www.intel.com',
        r'https://www.mydigitallife.net',
        r'https://docs.etf-validator.net',
        r'https://etf-validator.net',
        r'https://www.ogc.org',
        r'https://sourceforge.net',
        r'https://opensource.org',

        # link exists but when many link checks are done link checker fails
        # ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
        # Used in quickstart/osm_quickstart
        'https://www.openstreetmap.org/edit',

        # link exists but link check fails
        # SSL: CERTIFICATE_VERIFY_FAILED
        # Used in sponsors.rst
        'https://www.ntua.gr/en',
        'https://www.ice.ucdavis.edu/',

        # Link to the presentation
        r'presentation.html',

        # Ignore Stack Overflow links
        # as they return 429 Client Error: Too Many Requests for url
        # due to rate limiting
        r'https://stackoverflow'
        ]

linkcheck_anchors = False

# If false, no module index is generated.
#latex_use_modindex = True

# TODO (fgdrf) read the values from flat text file
# global replacements that will be included at the end of every source file
# see http://sphinx.readthedocs.org/en/latest/config.html#confval-rst_epilog
#
# TODO export versions into an extra app-versions file
#
rst_epilog="""
.. |osgeolive-project| replace:: %(projectname)s
.. |osgeolive-version| replace:: %(projectname)s %(projectversion)s
.. |sourceforge-download| replace:: https://sourceforge.net/projects/osgeo-live/files/%(projectversion)s/
.. |osgeo-download| replace:: https://download.osgeo.org/livedvd/releases/%(projectversion)s/
.. |osgeolive-hdspace| replace:: %(required_hd_space)02d GB
.. |osgeolive-iso-size| replace:: %(iso_size).1f GB
.. |osgeolive-vm-7z-size| replace:: %(vm_7z_size).1f GB
.. |osgeolive-appmenupath-geoserver| replace:: :menuselection:`Geospatial --> Web Services --> GeoServer --> Start GeoServer`
.. |osgeolive-appmenupath-udig| replace:: :menuselection:`Geospatial --> Desktop GIS --> uDig`
.. |osgeolive-appmenupath-52nWPS| replace:: :menuselection:`Geospatial --> Web Services --> 52North --> Start 52North WPS`
.. |osgeolive-appmenupath-ETF| replace:: :menuselection:`Geospatial --> Spatial tools --> ETF`
.. |vmdk| image:: /images/logos/vmdk.png
                        :align: bottom
                        :height: 18
.. |nologo| image:: /images/logos/nologo.png
                        :align: bottom
                        :height: 18
.. |osgeo_project| image:: /images/logos/OSGeo_compass.png
                        :alt: OSGeo Project
                        :align: bottom
                        :height: 18
                        :target: https://localhost/osgeolive/sponsors_osgeo.html
.. |osgeo_incubation| image:: /images/logos/OSGeo_compass_bw.png
                        :alt: OSGeo Community
                        :align: middle
                        :height: 18
                        :target: https://localhost/osgeolive/sponsors_osgeo.html
.. |osgeo_community| image:: /images/logos/OSGeo_compass_bw.png
                        :alt: OSGeo Community
                        :align: middle
                        :height: 18
                        :target: https://localhost/osgeolive/sponsors_osgeo.html
.. |CAT| replace:: `Catalogue Service <https://www.ogc.org/standards/cat>`__
.. |CSW| replace:: `Catalogue Service for the Web (CSW) <https://www.ogc.org/standards/cat>`__
.. |GML| replace:: `Geography Markup Language (GML) <https://www.ogc.org/standards/gml>`__
.. |FE| replace:: `Filter Encoding (FE) <https://www.ogc.org/standards/filter>`__
.. |ISO19105| replace:: `ISO 19105 <https://committee.iso.org/sites/tc211/home/projects/projects---complete-list/iso-19105.html>`__
.. |KML| replace:: `KML <https://www.ogc.org/standards/kml>`__
.. |OGCAPIFEATURES| replace:: `OGC API - Features <https://www.ogc.org/standards/ogcapi-features>`__
.. |ORM| replace:: `OGC Reference Model (ORM) <https://www.ogc.org/standards/orm>`__
.. |SENSORML| replace:: `Sensor Model Language (SensorML) <https://www.ogc.org/standards/sensorml>`__
.. |SFS| replace:: `Simple Feature Access (SFS) <https://www.ogc.org/standards/sfs>`__
.. |SFSQL| replace:: `Simple Features for SQL (SFS) <https://www.ogc.org/standards/sfs>`__
.. |SLD| replace:: `Styled Layer Descriptor (SLD) <https://www.ogc.org/standards/sld>`__
.. |SOS| replace:: `Sensor Observation Service (SOS) <https://www.ogc.org/standards/sos>`__
.. |WCPS| replace:: `Web Coverage Processing Service <https://www.ogc.org/standards/wcps>`__
.. |WCS| replace:: `Web Coverage Service (WCS) <https://www.ogc.org/standards/wcs>`__
.. |WMC| replace:: `Web Map Context (WMC) <https://www.ogc.org/standards/wmc>`__
.. |WMS| replace:: `Web Map Service (WMS) <https://www.ogc.org/standards/wms>`__
.. |WMTS| replace:: `OpenGIS Web Map Tile Service (WMTS) <https://www.ogc.org/standards/wmts>`__
.. |WFS| replace:: `Web Feature Service (WFS) <https://www.ogc.org/standards/wfs>`__
.. |WPS| replace:: `Web Processing Service (WPS) <https://www.ogc.org/standards/wps>`__
.. |OGC| replace:: `Open Geospatial Consortium (OGC) <https://www.ogc.org>`__
.. |OGCS| replace:: `OGC Standards <https://www.ogc.org/standards>`__
.. |SUPPORT| replace:: `OSGeo service providers <https://www.osgeo.org/service-providers>`__
.. |CC BY 3.0| replace:: `CC BY 3.0 <https://creativecommons.org/licenses/by/3.0/>`__
.. |CC BY-SA 3.0| replace:: `Creative Commons Attribution-ShareAlike 3.0 Unported (CC BY-SA 3.0) <https://creativecommons.org/licenses/by-sa/3.0/>`__
@OSGeoLiveDoc_menuselections@


@OSGeoLiveDoc_PROJECTS_LOGOS@
@OSGeoLiveDoc_PROJECTS_VERSIONS@""" % {
  'projectname':project,
  'projectversion': version,
  'required_hd_space': req_hd_size,
  'iso_size': iso_size,
  'vm_7z_size': vm_7z_size
}
