"""WP Suomi 2026: Going ACF-free. Kept out of git until the talk is given.

STARTING POINT ONLY. This built the first Going ACF-free.key on 24.9.2026. From
then on the .key is the source of truth and is edited in Keynote, by hand or by
AppleScript in place. Rebuilding from here would discard that work.
"""

EVENT = "WP Suomi 2026, Oulu, 16th of October, 2026"
RUNNING = "Going ACF-free"

# head is the Unbounded part, em the Instrument Serif italic part.
DECK = [
    dict(layout="cover", head="Going", em="ACF-free",
         standfirst=["Replacing a plugin dependency", "with core WordPress"]),

    dict(layout="about", sections=[
        ("About", "me", "Founder and CTO of Digitoimisto Dude Oy. Code for about thirty years, WordPress since 2005, online since 1999. Accessibility, open source, Linux servers, and building my own tools."),
        ("Dude &", "WordPress", "Contributing to WordPress core and plugins since we founded Dude in 2013. We maintain air-light, a starter theme with 1100 stars, and build business sites on it."),
    ], photos=["photos/rolle-90s.jpg", "photos/dudella.jpg"]),

    dict(layout="statement", head="A brief history of", em="fields and dependencies",
         standfirst=["How a blogging tool grew fields,", "and why blocks made it complicated."],
         notes="""Look a bit back before going forward. Fields first, then dependencies, then Gutenberg."""),

    dict(layout="pairs", head="Before", em="blocks", pairs=[
        ("2004", "WordPress 1.2 ships custom fields: a key, a value and a textarea."),
        ("2010", "WordPress 3.0 makes custom post types first class. Sites stop being blogs."),
        ("2011", "The first commit of Advanced Custom Fields lands on wordpress.org."),
        ("2013", "Dude is founded. From here on, every site we build ships with ACF."),
    ], notes="""Custom fields arrived in WordPress 1.2 "Mingus", 22.5.2004, the same release that introduced plugins.
ACF's first commit to the plugin directory was 28.3.2011, by Elliot Condon, who ran it alone for ten years.
Sources: wordpress.org/news/2004/05/heres-the-beef/ | wordpress.org/book/2015/11/wordpress-1-2-mingus/ | advancedcustomfields.com/blog/10-years-of-acf-a-truly-wonderful-time/"""),

    dict(layout="bullets", head="Knifing", em="the database", items=[
        "In the blogging days, meta fields were all we used, and that was enough.",
        "For a developer, get_post_meta() is fine. It is a knife straight into a row.",
        "The moment a client edits content, a knife is not a system.",
    ], notes="""I used to do WordPress with meta fields only, when it was only about blogging.
It works fine for a developer, it is kind of like knifing the database field.
But if the customer wants to update content easily, you need a system."""),

    dict(layout="pairs", head="So we needed", em="a system", pairs=[
        ("CMB", "Custom Metaboxes and Fields, rewritten by WebDevStudios as CMB2 in 2015."),
        ("Carbon Fields", "htmlBurger's in-house library since 2009, a public plugin from 2016."),
        ("ACF", "Fields with a UI a client could actually use. Quickly the industry standard."),
        ("Core", "No nice, fast way to add your own fields without writing custom code."),
    ], notes="""There were things like CMB2 and Carbon Fields, but we quickly settled on ACF. It was the industry standard in a sense, and WordPress had no nice and fast way to add custom fields without custom code.
Honest footnote: CMB2 (out of beta 2.2015) and the public Carbon Fields plugin (1.2016) postdate our switch; their predecessors were around before.
Sources: wptavern.com/custom-metaboxes-and-fields-for-wordpress-cmb2-now-out-of-beta | carbonfields.net/about/"""),

    dict(layout="statement", head="Every site we built", em="was an ACF site",
         standfirst=["For twelve years that was not a decision.", "It was the default."]),

    dict(layout="code", head="What that", em="looks like",
         left_label="The template", left_code="the_field( 'subtitle' );\nthe_field( 'hero_image' );\nthe_field( 'cta_url' );",
         right_label="The other source of truth", right_code="acf-json/group_5f3a.json\n\n  \"key\": \"field_5f3a1\",\n  \"name\": \"subtitle\",\n  \"type\": \"text\"",
         takeaway="The only things that know this field exists are the theme and a JSON file the theme ships. Nothing else on the site, and nothing outside it."),

    dict(layout="bullets", head="Every plugin is", em="a liability", items=[
        "WordPress works fine without plugins. For purists like me, fewer is better.",
        "Third-party code is code you did not write, did not review, and still ship.",
        "One careless plugin can query the database on every single page load.",
        "My own plugins excepted, obviously. Those are flawless.",
    ], notes="""Other dependencies too, not just fields. WordPress works fine without plugins, and for purists the fewer the better.
Third-party code is always a liability and makes sites slower, unless you audit each plugin carefully: no endless queries hitting the database on every load.
Last bullet is the joke. Pause for it.
So: fewer dependencies is a good thing. Hold that thought, Gutenberg is coming."""),

    dict(layout="pairs", head="The", em="bill", pairs=[
        ("Lock-in", "Remove the plugin and the site does not degrade. It renders blank."),
        ("No schema", "A field has a type in the admin and no type anywhere else."),
        ("No REST", "Your data is invisible to anything that is not PHP in your theme."),
        ("One owner", "And it is not you."),
    ]),

    dict(layout="pairs", head="October", em="2024", pairs=[
        ("The fork", "ACF was forked on wordpress.org into Secure Custom Fields."),
        ("Two plugins", "WP Engine still ships ACF. Shared history, separate futures."),
        ("Still open", "Two years on, there is no resolution to sit and wait for."),
        ("The real risk", "Your sites depend on the outcome of somebody else's lawsuit."),
    ]),

    dict(layout="statement", head="Then Gutenberg", em="moved the goalposts",
         standfirst=["WordPress 5.0, 6th of December 2018.", "The editor was now a React application."],
         notes="""Fewer dependencies is a good thing. But Gutenberg complicated it.
Source: wordpress.org/news/2018/12/bebo/"""),

    dict(layout="pairs", head="And suddenly we were", em="JS developers", pairs=[
        ("2012", "Underscores. PHP, HTML and CSS. Where I learned themes, and where I stayed."),
        ("Never", "Sage, Twig, Timber or Blade. My templates stayed plain PHP."),
        ("2017", "WordPress nearly dropped React over its patent clause. Facebook relicensed it as MIT."),
        ("2018", "Blocks are React components, built with npm and @wordpress/scripts."),
    ], notes="""I am a traditional WordPress guy. I come from the Underscores world, never got into Sage, Twig, Blade or other templating languages. PHP, HTML and CSS.
Then WordPress took a huge leap and moved to React.
Underscores launched 13.2.2012. Mullenweg announced dropping React on 14.9.2017 over the patents clause; Facebook relicensed React under MIT days later and Gutenberg stayed on React.
Sources: themeshaper.com/2012/02/13/introducing-the-underscores-theme/ | ma.tt/2017/09/on-react-and-wordpress/ | ma.tt/2017/09/facebook-dropping-patent-clause/"""),

    dict(layout="bullets", head="Where does a block", em="even live?", items=[
        "In the theme, in a plugin, one plugin per block, or all of them in one.",
        "Registered in PHP, in JS, or both. block.json from 5.5, canonical from 5.8.",
        "Built with @wordpress/scripts, your own webpack, or in wp-admin with no code.",
        "We had no idea how to build blocks. We only knew native was the way.",
    ], notes="""Suddenly an npm package for block scripts, blocks in the theme, as a plugin, many blocks in one plugin, in theme AND plugin, registered via JS or PHP or both, or built in wp-admin only, and so on and so on.
Suddenly we had no idea how to build blocks, but we knew the native way was the only way.
Sources: developer.wordpress.org/block-editor/reference-guides/packages/packages-scripts/ | make.wordpress.org/core/2021/06/23/block-api-enhancements-in-wordpress-5-8/"""),

    dict(layout="statement", head="So can core", em="do it yet?",
         standfirst=["Since 6.5, mostly.", "Since 6.9, properly."]),

    dict(layout="statement", head="The leap is high,", em="and that is not your fault",
         standfirst=["Ten years of Gutenberg,", "and nothing was ever taken away."]),

    dict(layout="list", head="Ways to build", em="a block", items=[
        "Core blocks, as shipped",
        "Core block variations",
        "Block patterns",
        "Block styles",
        "Filtering a core block in PHP",
        "Filtering a core block in JS",
        "register_block_type in PHP",
        "registerBlockType in JS",
        "block.json metadata",
        "Dynamic block with render.php",
        "Custom React block",
        "Custom block with InnerBlocks",
        "acf_register_block_type",
        "ACF blocks via block.json",
        "Hybrid ACF and native",
        "Classic theme, core blocks",
        "Block theme, full site editing",
        "Block Bindings",
    ]),

    dict(layout="bullets", head="Why there are", em="so many", items=[
        "Every approach that ever shipped still works. That is deliberate.",
        "Deprecation in WordPress means the old way keeps running forever.",
        "So the pile grows, and none of it is labelled start here.",
        "block.json is not the eighteenth option. It is the envelope for the rest.",
    ]),

    dict(layout="pairs", head="The docs are", em="scattered", pairs=[
        ("The handbook", "Correct, enormous, and organised for people who already know."),
        ("Dev notes", "The real documentation, published once, on a blog, and never revised."),
        ("Trac and GitHub", "Where behaviour is actually decided, and never summarised."),
        ("A Slack thread", "Where your answer was posted in 2024 and then scrolled away."),
    ]),

    dict(layout="pairs", head="What actually", em="changed", pairs=[
        ("6.5", "March 2024. Block Bindings lands with a post meta source."),
        ("6.6", "Bound attributes become visible in the block sidebar."),
        ("6.7", "November 2024. An editor UI, and bound meta you can type into."),
        ("6.9", "December 2025. Custom sources get a real UI. This is the one."),
    ]),

    dict(layout="statement", head="In 6.5 it was a demo.", em="In 6.9 it is a tool.",
         standfirst=["Which means the answer to", "“can core do this” changed ten months ago."]),

    dict(layout="pairs", head="Four", em="decisions", pairs=[
        ("Data", "A value an editor types. register_post_meta, then bind it."),
        ("Layout", "An arrangement of blocks that already exist. That is a pattern."),
        ("Behaviour", "Something that moves on the front end. Interactivity API."),
        ("Composition", "The editor needs to nest things. InnerBlocks, and only then."),
    ]),

    dict(layout="code", head="One field,", em="two ways",
         left_label="With the plugin", left_code="the_field( 'subtitle' );",
         right_label="With core", right_code="register_post_meta( 'post', 'subtitle', [\n  'type'         => 'string',\n  'single'       => true,\n  'show_in_rest' => true,\n] );",
         takeaway="Four more lines, and the value now has a type, a schema and a REST route. The theme stops being the only thing that knows the field exists."),

    dict(layout="bullets", head="What that", em="buys you", items=[
        "A type and a schema, enforced rather than merely documented.",
        "A REST route, so the app, the importer and the editor all see the same field.",
        "Revisions, because core knows the value is there.",
        "A site that still renders when the plugin is gone.",
    ]),

    dict(layout="code", head="Binding it to", em="a core block",
         left_label="The old way", left_code="acf_register_block_type( [\n  'name'            => 'subtitle',\n  'render_template' => 'blocks/subtitle.php',\n] );",
         right_label="The binding", right_code="<!-- wp:paragraph {\n  \"metadata\": { \"bindings\": {\n    \"content\": {\n      \"source\": \"core/post-meta\",\n      \"args\": { \"key\": \"subtitle\" }\n    } } } } -->",
         takeaway="No custom block, no render template, no plugin. A core paragraph that reads your meta, and an editor who can still style it like any other paragraph."),

    dict(layout="bullets", head="What just", em="happened", items=[
        "The block is core, so it keeps every feature core adds to it later.",
        "The value is meta, so the REST API and wp-cli already understand it.",
        "The binding is markup, so it lives in the pattern, not in a PHP file.",
        "Nothing here is yours to maintain.",
    ]),

    dict(layout="code", head="Editing it in", em="the editor",
         left_label="Register with a label", left_code="register_post_meta( 'post', 'subtitle', [\n  'type'         => 'string',\n  'single'       => true,\n  'show_in_rest' => true,\n  'label'        => 'Subtitle',\n] );",
         right_label="What you get", right_code="Attributes panel lists the field.\nBound text is editable in place.\nString and rich text only.\n\nSince 6.7.",
         takeaway="This is the part that decides whether a client will accept the change. Until 6.7 the answer was no, because a bound value was read-only in the editor."),

    dict(layout="code", head="Your own", em="source",
         left_label="Register the source", left_code="register_block_bindings_source(\n  'dude/settings', [\n    'label'              => 'Site settings',\n    'get_value_callback' => $cb,\n  ]\n);",
         right_label="Give it a UI", right_code="// 6.9, in JS\nregisterBlockBindingsSource( {\n  name: 'dude/settings',\n  getFieldsList: () => fields,\n} );",
         takeaway="Before 6.9 a custom source worked but was invisible, so only a developer could use it. getFieldsList is what turns it into something an editor can pick from a menu."),

    dict(layout="pairs", head="It was a pattern", em="all along", pairs=[
        ("The tell", "The block has no data of its own. It only arranges other blocks."),
        ("The cost", "A custom block is code you version, test and migrate forever."),
        ("The pattern", "A PHP file of block markup, registered once, edited by anyone."),
        ("The count", "Roughly half the custom blocks we ever wrote were patterns."),
    ]),

    dict(layout="code", head="Extend, do not", em="replace",
         left_label="A new block", left_code="// 200 lines of JS\n// a build step\n// a migration when core\n// changes the markup",
         right_label="A style on the core one", right_code="register_block_style( 'core/quote', [\n  'name'  => 'pull',\n  'label' => 'Pull quote',\n] );",
         takeaway="Most custom blocks in an agency codebase are a core block with a different look. A style, a variation or a render_block filter gets you there without owning a block."),

    dict(layout="code", head="When you do", em="need one",
         left_label="block.json", left_code="{\n  \"apiVersion\": 3,\n  \"name\": \"dude/timeline\",\n  \"title\": \"Timeline\",\n  \"render\": \"file:./render.php\",\n  \"attributes\": {\n    \"year\": { \"type\": \"string\" }\n  }\n}",
         right_label="render.php", right_code="<div <?php echo get_block_wrapper_attributes(); ?>>\n  <?php echo esc_html( $attributes['year'] ); ?>\n  <?php echo $content; ?>\n</div>",
         takeaway="One JSON file and one PHP file. No build step, no React, no node_modules. This is the block you write when the shape genuinely does not exist yet."),

    dict(layout="bullets", head="Let the client", em="compose", items=[
        "InnerBlocks is the honest answer to “can we add another one of these”.",
        "allowedBlocks narrows it enough that the layout cannot be broken.",
        "The template attribute gives them a sensible starting arrangement.",
        "Every block inside stays core, so you inherit core's improvements for free.",
    ]),

    dict(layout="code", head="Front end,", em="no build step",
         left_label="What we used to ship", left_code="// jQuery, or a bundle,\n// or a block that re-renders\n// the whole thing in React",
         right_label="Interactivity API", right_code="<div data-wp-interactive=\"dude/faq\"\n     data-wp-on--click=\"actions.toggle\"\n     data-wp-class--is-open=\"context.open\">",
         takeaway="Directives in the markup, state handled by core. This is the piece that removes the last reason most agency themes still carry a bundler."),

    dict(layout="bullets", head="theme.json is", em="the contract", items=[
        "Palette, type scale and spacing declared once, in one file.",
        "The editor renders what the front end renders, because both read it.",
        "Contrast is a decision you make in the file, not per block, per site.",
        "This is the slide that matters if you have ever presented in a bright room.",
    ]),

    dict(layout="pairs", head="One field group,", em="end to end", pairs=[
        ("Before", "Six ACF fields, one render template, one acf-json file."),
        ("Step one", "register_post_meta for each field, with show_in_rest and a label."),
        ("Step two", "A pattern of core blocks, with bindings pointing at those keys."),
        ("After", "No plugin in the dependency list, and the same page on screen."),
    ]),

    dict(layout="bullets", head="Moving", em="the data", items=[
        "ACF stores the value in postmeta under the field name. That part is easy.",
        "It also stores a companion key prefixed with an underscore. Drop it.",
        "Repeaters are stored as a count plus indexed keys. That part is not easy.",
        "wp-cli, a dry run, and a staging copy. Never in place, never on a Friday.",
    ]),

    dict(layout="pairs", head="We built", em="a converter", pairs=[
        ("What it does", "Reads an ACF block and writes block.json, render.php and the editor script."),
        ("How", "An agent does the conversion. The tool is the harness, not the intelligence."),
        ("Where it is", "The output compiles. It has never been loaded in a real editor yet."),
        ("What it taught us", "It emitted a custom block where a pattern belonged. Valid is not correct."),
    ]),

    dict(layout="bullets", head="Learning this", em="with AI", items=[
        "The docs are scattered, which is exactly the shape of problem a model is good at.",
        "It has read every version, so it will hand you the 2019 way with total confidence.",
        "Make it cite the handbook page. Then go and read the handbook page yourself.",
        "Never ship a block you cannot defend in code review. That is the whole rule.",
    ]),

    dict(layout="pairs", head="Where ACF", em="still wins", pairs=[
        ("Repeater", "Core has no equivalent. InnerBlocks is close and is not the same."),
        ("Flexible content", "A page builder in a field. Nothing in core is trying to be this."),
        ("Options pages", "Site-wide settings with a real UI, still a plugin problem."),
        ("Relationships", "Picking posts, terms and users, with a UI a client can use."),
    ]),

    dict(layout="bullets", head="And the fork", em="does not help", items=[
        "Secure Custom Fields ships without Repeater and Flexible Content.",
        "No Options Pages, no Gallery, no Clone. Those were always Pro features.",
        "So the free fork is not the escape hatch people assume it is.",
        "Which is the argument for moving the simple eighty per cent to core.",
    ]),

    dict(layout="statement", head="Core first.", em="ACF where it earns it.",
         standfirst=["Not a migration project.", "A default that changed."]),

    dict(layout="bullets", head="What changes", em="in your week", items=[
        "You write less code, and you read more handbook. That is a real cost.",
        "Field changes become code review, not a click in the admin.",
        "Your editors get a better editor, which is the part they will notice.",
        "Your next site starts from patterns instead of from a plugin.",
    ]),

    dict(layout="bullets", head="Start on", em="Monday", items=[
        "Pick one field group, not one site.",
        "Pick the simplest one: text, an image, a link. Those bind today.",
        "Ship it on one template, keep ACF installed, and compare.",
        "Then decide. You do not have to be right about all of this at once.",
    ]),

    dict(layout="pairs", head="Where to", em="read next", pairs=[
        ("The handbook", "developer.wordpress.org, the Block Bindings reference."),
        ("Dev notes", "make.wordpress.org/core, tagged 6.5, 6.7 and 6.9."),
        ("air-light", "github.com/digitoimistodude/air-light, where we test this."),
        ("These slides", "github.com/rollecode, with the code samples that fit."),
    ]),

    dict(layout="statement", head="Kiitos.", em="Questions?",
         standfirst=["Rolle Laukkarinen", "rolle.social"]),
]

LOGO = ("wpsuomi-logo.svg", "wpsuomi.png", 57, "WP Suomi")
VENUE = "Sisu Talk, main stage, Hotel Lasaretti, Oulu"
SLOT_MIN = 45
QA_MIN = 10
KEY_NAME = "Going ACF-free"

NOTES = """
## Before the stage

- Run the 6.9 bindings UI yourself on a fresh install. The screenshots on the
  editor and custom-source slides must be your own, from the current version
- Confirm the string and rich text limitation still holds in 6.9 for the
  built-in post meta source
- Check whether getFieldsList needs a JS build step, because that changes the
  "no build step" claim on the Interactivity slide
- Pick the real field group for "One field group, end to end" and walk it
- Time Act 3 out loud. Fifteen minutes of code slides always runs long

## Kept off the slides on purpose


## Editing this

Slide copy lives in DECK in talks/wpsuomi-2026/talk.py. Change it there, then:

    python3 deck.py talks/wpsuomi-2026

The Keynote build refuses to run without --force, because it replaces
Going ACF-free.key wholesale.
"""
