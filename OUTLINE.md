# Going ACF-free

The running order and speaker notes of `Going ACF-free.key`, exported from the deck on 9.10.2026.

WP Suomi 2026, Friday 16.10.2026 at 14:10, main stage, Hotel Lasaretti, Oulu. The slot is 45 minutes: 35 minutes of talk and 10 minutes of Q&A. The deck has 44 slides.

## Running order

The minute column shows how far into the talk each slide should end, based on `minutes.json`.

| # | Slide | Minute |
| -- | -- | -- |
| 1 | Going ACF-free | 0.3 |
| 2 | About Rolle / Dude & WordPress | 1.6 |
| 3 | No shame in using ACF or plugins | 2.1 |
| 4 | A quick poll | 2.9 |
| 5 | A quick poll, question 1 | 3.8 |
| 6 | A quick poll, question 2 | 4.7 |
| 7 | A quick poll, question 3 | 5.5 |
| 8 | What is a dependency? | 6.4 |
| 9 | A brief history of fields and dependencies in WordPress | 6.8 |
| 10 | Fields since 2004 | 8.2 |
| 11 | First there were Advanced Custom fields (Advanced struck out) | 8.6 |
| 12 | No dependencies? Let’s knife the database! | 9.1 |
| 13 | Using (prehistoric) custom fields | 10.6 |
| 14 | Advanced Custom Fields | 11.0 |
| 15 | We thought we did “the core way” | 11.9 |
| 16 | So what’s the answer? | 12.3 |
| 17 | We thought “native” meant React.js | 13.2 |
| 18 | And suddenly we were JS-devs | 13.6 |
| 19 | Media and text, coded by hand | 14.5 |
| 20 | React is for WordPress core developers | 14.9 |
| 21 | True dependency-free WordPress | 15.3 |
| 22 | Three ways to build a sovereign theme | 16.2 |
| 23 | From Traditional to Modern | 17.1 |
| 24 | Going 100% core: pros | 17.9 |
| 25 | Content in ACF and in core | 19.3 |
| 26 | From server to browser | 20.7 |
| 27 | Going 100% core: the “cons” | 21.5 |
| 28 | The designer’s new job | 22.4 |
| 29 | The leap is high, and that is not your fault | 22.8 |
| 30 | Ways to build a block | 24.2 |
| 31 | From core to custom, prioritized | 25.1 |
| 32 | Block example: Media and text | 25.9 |
| 33 | Most of the time you don’t need to code a block | 26.4 |
| 34 | When you do code: the Dude House Way | 27.2 |
| 35 | Site Editing/Block theme: our first build | 28.1 |
| 36 | Fields outside blocks, without ACF | 29.0 |
| 37 | This is a lot, where to start, going 100% ACF-free? | 29.4 |
| 38 | It has always been a pattern | 30.3 |
| 39 | Start every page from a pattern | 31.1 |
| 40 | What does it look like? | 32.0 |
| 41 | Learning this with your AI | 32.8 |
| 42 | When ACF still makes sense | 33.7 |
| 43 | Further reading | 34.6 |
| 44 | Kiitos. | 35.0 |

## Speaker notes

### 1. Going ACF-free

Hello everyone, I am Rolle from Dude.
This talk is about replacing ACF with core WordPress.
We used ACF for ten years, and only recently moved on to core blocks.
I will share what we learned on the way.

### 2. About Rolle / Dude & WordPress

Most of you already know me, so I keep this short.
I am the founder and CTO of Dude, and I have built WordPress sites since 2005.

### 3. No shame in using ACF or plugins

Nobody gets shamed today for using ACF or plugins.
We used ACF for more than ten years, and it built a lot of good sites.
ACF solved a real problem back when core could not.
Core can do much more today, and this talk is about that.
Nobody here is going to ask who the hell still uses ACF. Not today.

### 4. A quick poll

Ask for hands up on each option.
Get the room to answer before I say anything about going ACF-free.

### 5. A quick poll, question 1

Hands up for option 1: ACF on every site, for everything.

### 6. A quick poll, question 2

Hands up for option 2: ACF for some things, core blocks for the rest.

### 7. A quick poll, question 3

Hands up for option 3: ACF is legacy, and you have moved on to native or core blocks.
Say the split out loud. It shows how much of this talk is new to the room.

### 8. What is a dependency?

I could talk for hours about dependencies, so we start with a definition.
WordPress itself is a dependency too.
A site depends on the host, Linux, the web server, PHP, the database, WordPress, the theme, the plugins and outside services like DNS and email.
A site always has dependencies, so the goal is to choose them on purpose.
A good dependency has an open licence, can be replaced, keeps your data in a standard format and outlives the site.
WordPress core passes all four: GPL, over 20 years old, thousands of contributors and plain database tables.
A plugin owning your content format does worse on every check. ACF is that kind of plugin.

### 9. A brief history of fields and dependencies in WordPress

First a short look back.
Fields come first, then dependencies, then Gutenberg.

### 10. Fields since 2004

Custom fields have been in core since WordPress 1.2 in 2004. I started with WordPress in 2005.
2010: WordPress 3.0 brings custom post types.
2011: ACF gets its first commit.
2014: our starter stack dudestack required ACF from its first commit.
2018: WordPress 5.0 ships Gutenberg, built on React.
2019: ACF Blocks put fields inside blocks.
2021: WordPress 5.8 brings theme.json and block.json.
2022: WP Engine buys ACF.
2024: Block Bindings arrive in 6.5, and ACF is forked as Secure Custom Fields.
2025: WordPress 6.9 gives bindings a real UI, and we build our first native blocks at Dude.
2026: WordPress 7.

### 11. First there were Advanced Custom fields (Advanced struck out)

ACF means Advanced Custom Fields. Drop the word Advanced and you get plain custom fields.
Core has had custom fields since 2004.
A field is a named value on a post: a key and a value in wp_postmeta.

### 12. No dependencies? Let’s knife the database!

This is a bit of a joke, but it is real history.
We used to build sites with meta fields only, back when WordPress was a blogging tool.
Meta fields work fine for a developer. It feels like knifing the database.
A client needs a real system to update content easily.
If asked: the box only ever did text. wp_postmeta stores every value as a string, with no type column.
If asked: featured images arrived in WordPress 2.9 in 2009 and took over the main job of the box. That explains the best before 2009 stamp.

### 13. Using (prehistoric) custom fields

A fun aside. I do not recommend this box for client sites.
To turn it on: Options, Preferences, General, Advanced, Custom fields. The editor reloads.
ACF hides the box by default. The ACF filter on the slide brings it back.
ACF hides it because the box runs a slow query over the whole wp_postmeta table.
The box only does text. Keys are typed by hand, so Photo credit and photo_credit become two different fields.
Today register_post_meta() and Block Bindings do the job properly.
The 100% dependency-free stamp is true. No plugin is involved.

### 14. Advanced Custom Fields

ACF got its first commit on 28.3.2011.
ACF made custom fields usable with field types, a real UI and repeaters.
Everything ACF adds is still a field in wp_postmeta, printed by a template.
Blocks changed the unit of content from a field to a block. This talk is about that change.

### 15. We thought we did “the core way”

I have always liked the core way of WordPress. air-light started from Automattic's Underscores in 2016.
We felt we did things the core way, but we still used ACF. With ACF it is not the core way.
You do not want to be a purist. You want something fast to build that works for years.
ACF was that, until it wasn't.
air-light still ships no blocks, on purpose. For a long time I saw blocks as a dependency too.
If asked: our first native block code in air-light is from 28.2.2025.

### 16. So what’s the answer?

For years our answer was Gutenberg for articles and ACF for everything else.
In 2018 I did not even have time to test Gutenberg properly.
When we went native in 2025, we thought blocks meant React. So we coded every block ourselves, with every option in React.
The GIF is Deep Thought from The Hitchhiker's Guide to the Galaxy. The answer was 42, and just as useful.

### 17. We thought “native” meant React.js

2017: we added the Classic Editor to our stack to prepare for Gutenberg.
2018 to 2020: Gutenberg for articles only. Pages stayed on ACF.
2021: ACF blocks became our standard.
In 2018 a custom block needed JavaScript and a build step. PHP developers did not want to write React, so ACF Blocks, Block Lab and Lazy Blocks appeared.
2025: our first native blocks, with every option written in React.
The peak was one client site in 2026: 23 custom blocks and about 4,130 lines of JavaScript.
Markup coded into the blocks hurt the most. A pattern could not drop the buttons, because the buttons were in the code.
From 5.2026 that site moved to core Group blocks and patterns.

### 18. And suddenly we were JS-devs

I am a traditional WordPress developer. I come from Underscores, with PHP, HTML and CSS.
I never got into Sage, Twig, Blade or other templating languages.
Then WordPress took a huge leap and moved to React.
Learning React still paid off. It taught us how the block editor works, and now we can tell when a custom block is really needed.

### 19. Media and text, coded by hand

This is the media and text block coded by hand, the way we built blocks in 2025 and 2026.
Nine files. Every option needs an attribute in block.json and a control in edit.js.
save.js must print the same HTML as the database, or the editor marks the block invalid.
The core Media & Text block already has all these controls. It has been in core since WordPress 5.0 in 2018.
Our sidebar text fields lost bold text, links and lists.
We maintained all this code ourselves, while core maintains the same block for free.
Since 2021, theme.json can style the core Media & Text block fully, with no code.

### 20. React is for WordPress core developers

The block editor is built with React. React is for the people building WordPress core.
Themes, patterns, block styles and theme.json need no React. They are HTML and JSON.
You can build custom blocks without JSX or a build step.
On the front end, the Interactivity API works without React.

### 21. True dependency-free WordPress

Jokes aside, dependency-free here means no plugin owns the content.
WordPress itself is the one dependency we choose on purpose.
The rest of the talk shows our route away from ten years of ACF.

### 22. Three ways to build a sovereign theme

I stuck to PHP, HTML and CSS and the core way. The core way avoids vendor lock-in, and it feels good to build things the way core intended.
Traditional: Underscores from Automattic, launched in 2012. PHP templates and the template hierarchy.
Innovative: Sage by Roots, started in 2011. Blade views, Composer and Vite.
Modern: block themes since WordPress 5.9 in 2022. HTML templates and theme.json, edited in the Site Editor.

### 23. From Traditional to Modern

You do not have to jump in one go. Every step works inside a classic theme, and that makes a hybrid theme.
Step 1: replace ACF blocks with core blocks, patterns and your own blocks.
Step 2: replace ACF fields with register_post_meta() and Block Bindings.
Step 3: add theme.json to the classic theme.
Step 4: add block template parts for the header and footer.
The last step is a full block theme with HTML templates.
A hybrid theme is a fine place to stop.
If asked about full site editing: block themes had 8.3% of non-default theme installs in June 2026. Classic themes still win about 11 to 1.
If asked: templates edited in the Site Editor are saved to the database and drift from git.

### 24. Going 100% core: pros

Performance: work moves from the server to the browser. The next slide shows the difference.
The basics are built in: heading levels, colours and spacing. With ACF, even changing an h1 to an h2 was a job for a developer.
Our editors could not add bold text or a link in the middle of a sentence in the ACF WYSIWYG field.
The client edits in the preview. Our big ACF blocks flickered every time you touched them.
Lego and Duplo at once: big and small pieces, mixed freely.
A client once called an old site "the WordPress straitjacket Dude knitted". He was half joking.

### 25. Content in ACF and in core

With ACF, things live in four places: field groups in the database, the ACF plugin, PHP templates and wp_postmeta.
Lose the database and you lose the field groups. ACF added Local JSON in 2014 to copy them into the theme for git.
Many of us built field groups in code instead, with acf_add_local_field_group() or ACF Codifier. That adds one more dependency on top of ACF.
With core blocks there are three places and no plugin: the block in core, the styles in theme.json and the content in post_content.
There are no field groups to set up. The block is the field.

### 26. From server to browser

With ACF, PHP renders every block on every cache miss and reads the fields one at a time from the database.
With core blocks, the block markup is already saved in the page, so there is nothing to build.
Only the live parts, like a job listing, fetch data from the REST API in the browser.
A cache hit ends the request in both cases.

### 27. Going 100% core: the “cons”

The cons: a steep learning curve for the whole team.
Less PHP and more JSON, in theme.json and block.json.
Old habits to unlearn: we used to build every block from scratch.
Heavy build tooling for custom blocks: React, npm and a build step.
Core moves fast, and the docs are scattered.
I said this would take our team a year or more to absorb. It is wonderful and horrible at the same time.

### 28. The designer’s new job

Designers used to limit the client. Now the client gets full freedom.
Every block has to look like the client's brand in any combination.
With great power comes great responsibility.
The design system lives in theme.json, block styles and patterns. We lock the parts that must not change.
We give as many choices as we can and make them all look good.

### 30. Ways to build a block

There are 21 ways to build a block. No wonder moving off ACF feels confusing.
You do not need all of them.
Column 1 needs no custom code: core blocks, variations, patterns, styles and synced patterns.
Column 2 is your own code: block.json, render.php, React, InnerBlocks and the Interactivity API.
Column 3 has the in-betweens and third parties: ACF blocks, Block Bindings and page builders.
Elementor stores layouts as JSON in post meta, so the content needs the plugin. Same problem as ACF, only bigger.

### 31. From core to custom, prioritized

Go in this order: core blocks, then patterns, then variations and styles.
Write a custom block only when nothing above fits.
If asked: 115 is the core block count in WordPress 7.1.

### 32. Block example: Media and text

The same block, built two ways.
Left: our most recent ACF site, launched in 5.2026. The editor fills a fixed form with a title, a text box, a link and an image.
Every new variation needs a developer to add a field.
Right: the core Media & Text block, in core since WordPress 5.0. There is nothing to build.
The client can put any blocks inside it, like headings, lists and buttons.
theme.json and block styles handle the look. A pattern file gives editors a ready starting point.

### 33. Most of the time you don’t need to code a block

Search the inserter first. The core block often already exists.
One of our 2026 sites has zero custom blocks: core blocks, three block styles, theme.json and patterns.

### 34. When you do code: the Dude House Way

When we do write code, we follow this order at Dude.
1. Lock theme.json first: palette, type scale and spacing. The client picks from our scale.
2. Core blocks by default, curated per post type.
3. Style core blocks in theme.json. SCSS only for the rest.
4. Layouts are patterns. We deleted custom blocks that were only layout.
5. Public data comes from the REST API and renders in the browser. We avoid render.php.
6. Interactive parts use the Interactivity API. No React on the front end.
7. A custom block is the last resort.
ACF is still installed on these sites, but it builds no blocks. It handles data forms like settings screens.
If asked: some of our current blocks still use render.php, and we are moving away from it.

### 35. Site Editing/Block theme: our first build

Our first full site editing build was a small route guide site, from 5.2026 to 6.2026.
Templates and parts are HTML files. theme.json turns off custom colours and sizes.
No custom blocks and no ACF. Editors change the header, footer and menus in the Site Editor.
Lesson 1: git and the database drift apart. A Site Editor change on production stays in the database. Decide up front if files or the database own the templates.
Lesson 2: core Navigation does not suit a sidebar menu. We solved it with our own JS and SCSS.
Lesson 3: multilingual was hard with Polylang.

### 36. Fields outside blocks, without ACF

So far it was all page content. Custom post types and their fields work without ACF too.
register_post_type() goes in the theme. It has been in core since 2010.
register_post_meta() adds the fields, and Block Bindings show them. The editor edits them in place.
Templates and the Query Loop block handle single and archive pages.
ACF still makes sense for repeaters, relationships and options pages. Core has no editing UI for those.

### 37. This is a lot, where to start, going 100% ACF-free?

If you take one thing home, take patterns.
Patterns need no code and work in every theme, classic or block.
They are the fastest way away from ACF blocks.

### 38. It has always been a pattern

We went through the 49 ACF blocks of one client site. 32 of them only printed layout and text.
Every one of them could have been a pattern.
A pattern is core blocks arranged once and saved. The client can change anything in it.
Patterns have been in core since WordPress 5.5 in 2020.

### 39. Start every page from a pattern

New from the last weeks.
A new empty page opens on a blank canvas, and clients do not find the finished sections.
The core pattern window only shows patterns registered for post content. Patterns saved in the editor never show there.
Left: the core way, for patterns in theme files.
Right: our fix for editor-saved patterns. A new empty page opens the inserter on the Patterns tab.
This is coming to air-helper, on by default, with a filter to turn it off.
If asked: it uses __experimental props, so we recheck it on every major release.

### 40. What does it look like?

The client opens a new page, and the Patterns tab is already open.
The finished sections are right there. Drag one in and edit it.

### 41. Learning this with your AI

AI is great for learning this, with one caution.
AI makes the same mistakes we did. Ask for a block and it often writes a full React block.
Give it the priority order first: core blocks, patterns, block styles, and a custom block last.
Ask it to show the handbook page behind the answer. Review the code like a colleague's code.

### 42. When ACF still makes sense

ACF is still the better choice in a few places.
Integrations: Polylang, FacetWP, Relevanssi and SEO plugins read ACF fields directly.
Settings pages: an ACF options page takes a few lines.
Relationships: ACF has a ready picker. Core stores the link but has no UI for it.
Structured data like product specs, opening hours and event dates needs a form.
The rule: pages and layouts with core blocks and patterns, structured data with the easiest form. Often that is still ACF.
