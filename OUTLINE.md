# Going ACF-free

The running order and speaker notes of `Going ACF-free.key`, exported from the deck on 26.9.2026.

WP Suomi 2026, Thursday 16.10.2026 at 14:10, main stage, Hotel Lasaretti, Oulu. The slot is 45 minutes: 35 minutes of talk and 10 minutes of Q&A. The deck has 42 slides.

## Running order

The minute column shows how far into the talk each slide should end, based on `minutes.json`.

| # | Slide | Minute |
| -- | -- | -- |
| 1 | Going ACF-free | 0.5 |
| 2 | About Rolle / Dude & WordPress | 2.2 |
| 3 | No shame in using ACF or plugins | 2.7 |
| 4 | A quick poll | 3.0 |
| 5 | A quick poll, question 1 | 3.4 |
| 6 | A quick poll, question 2 | 3.7 |
| 7 | A quick poll, question 3 | 4.3 |
| 8 | What is a dependency? | 5.2 |
| 9 | A brief history of fields and dependencies in WordPress | 5.5 |
| 10 | Fields and blocks since 2005 | 6.8 |
| 11 | Advanced Custom fields (Advanced struck out) | 7.2 |
| 12 | No dependencies? Let’s knife the database! | 8.3 |
| 13 | How to use (prehistoric) custom fields | 9.4 |
| 14 | Advanced Custom Fields since 2011 | 9.9 |
| 15 | We thought we did “the core way” | 11.0 |
| 16 | So what’s the answer? | 11.5 |
| 17 | We thought “native” meant React.js | 12.5 |
| 18 | And suddenly we were JS devs | 13.6 |
| 19 | Media and text, coded by hand | 14.5 |
| 20 | React is for WordPress core developers | 15.1 |
| 21 | Where your content lives | 16.4 |
| 22 | True dependency-free WordPress is the core way | 17.0 |
| 23 | Three ways to build a sovereign theme | 18.0 |
| 24 | From Traditional to Modern | 19.3 |
| 25 | Why go 100% core | 20.7 |
| 26 | The designer’s new job | 21.6 |
| 27 | The leap is high, and that is not your fault | 22.1 |
| 28 | Ways to build a block | 23.2 |
| 29 | From core to custom, prioritized | 24.3 |
| 30 | Block example: Media and text | 25.2 |
| 31 | Most of the time you don’t need to code a block | 25.6 |
| 32 | When you do code: the Dude House Way | 27.0 |
| 33 | Site Editing/Block theme: our first build | 28.3 |
| 34 | Fields outside blocks, without ACF | 29.6 |
| 35 | This is a lot, where to start, going 100% ACF-free? | 29.9 |
| 36 | It has always been a pattern | 30.9 |
| 37 | Start every page from a pattern | 32.0 |
| 38 | What does it look like? | 32.5 |
| 39 | Learning this with your AI | 33.5 |
| 40 | When ACF still makes sense | 34.5 |
| 41 | Where to read next | 35.0 |
| 42 | Kiitos. Questions? | 35.0 |

## Speaker notes

### 3. No shame in using ACF or plugins

Before the poll: this is not a talk about shaming anyone. There is no guilt in using plugins, dependencies or ACF. We used ACF for more than ten years and it built a lot of good sites.
I'd rather we all look at it positively: ACF solved a real problem when core couldn't. The question now is only what core can do for us today.
So when I ask who still uses ACF for everything, raise your hand. Nobody here is going to ask "who the hell still uses ACF". Not today.

### 4. A quick poll

Hands up. Get the room to commit before I say anything about going ACF-free.

### 5. A quick poll, question 1

Hands up. Get the room to commit before I say anything about going ACF-free.
Option 1: ACF on every site, for everything.

### 6. A quick poll, question 2

Option 2: ACF for some things, native blocks or core for the rest.

### 7. A quick poll, question 3

Option 3: ACF is legacy, moved on to native blocks, React blocks or core Gutenberg blocks.
Read the split out loud. It tells you how much of the next half hour is news to this room.

### 8. What is a dependency?

I could lecture a couple of hours when dependencies are an issue and when they are not, when properly used. But we need a definition. Then the honest question: is WordPress itself a dependency? Yes. A website on a server depends on the hardware or the host, Linux, the web server, PHP, the database, WordPress core, the theme, the plugins, and outside services like DNS, CDN, email and AI APIs. Every layer is something the site cannot continue normally without.
So the goal of this talk is not zero dependencies. The goal is choosing them on purpose, with four questions: who controls it, can I replace it, does my data come out in a standard format, and will it outlive the site.
WordPress core does well on all four: GPL licence, over 20 years old, thousands of contributors, and content stored in plain database tables. A plugin that owns your content format does worse on every one of them, which is where ACF comes in.

### 9. A brief history of fields and dependencies in WordPress

Look a bit back before going forward. Fields first, then dependencies, then Gutenberg.

### 10. Fields and blocks since 2005

Twenty-one years in one line. I start in 2005; custom fields had been in core since WordPress 1.2 in 2004.
2010 WordPress 3.0 makes custom post types first class. 2011 ACF's first commit (Elliot Condon). 2014 dudestack, our WordPress starter stack: its first commit on 25.2.2014 already requires wpackagist/advanced-custom-fields (github.com/digitoimistodude/dudestack). Dude itself was founded in 2013.
2018 WordPress 5.0 ships Gutenberg, a React editor, 6.12.2018. 2019 ACF 5.8 adds ACF Blocks, May 2019.
2021 WordPress 5.8: theme.json arrives, block.json becomes the canonical way to register blocks.
2022 WP Engine buys ACF with the other Delicious Brains plugins, June 2022. 2024 Block Bindings in 6.5 (March), and ACF is forked on wordpress.org as Secure Custom Fields (October).
2025 WordPress 6.9 gives custom binding sources a real UI, December 2025. 2026 here we are.
Sources: wordpress.org/news/2010/06/thelonious/ | advancedcustomfields.com/blog/acf-5-8-introducing-acf-blocks-for-gutenberg/ | make.wordpress.org/core/2021/06/25/introducing-theme-json-in-wordpress-5-8/ | deliciousbrains.com/epic-wordpress-announcement/ | make.wordpress.org/core/2024/03/06/new-feature-the-block-bindings-api/ | wptavern.com/acf-plugin-forked-to-secure-custom-fields-plugin | make.wordpress.org/core/2025/11/12/block-bindings-improvements-in-wordpress-6-9/

### 11. Advanced Custom fields (Advanced struck out)

ACF stands for Advanced Custom Fields. Take away the "Advanced" and what is left is custom fields, the same thing core has had since 2004.
What is a field? A named value attached to a post: a key and a value in wp_postmeta. We are talking about fields, right?

### 12. No dependencies? Let’s knife the database!

Well, this is a bit of a joke, but it has a place in history. We used to do WordPress with meta fields only, when it was only about blogging.
It works fine for a developer, it is kind of like knifing the database field.
But if the customer wants to update content easily, you need a system.

If someone asks: the original Custom Fields box only ever did text. A name, a value, a textarea.
Storage: wp_postmeta has four columns, meta_id, post_id, meta_key and meta_value, and meta_value is LONGTEXT. There is no type column, then or now.
Arrays and objects saved from code get PHP-serialized into that string. One key can hold many rows; get_post_meta() returns the first or all of them.
Keys starting with an underscore are hidden from the box. That is where ACF keeps its field reference, e.g. _subtitle = field_5f3a1.
The box is still in core in 7.1, just off by default in the block editor: Options menu (three dots), Preferences, General, Advanced, Custom fields. Turning it on reloads the editor. It only shows for post types that support custom-fields, and ACF removes it by default (remove_wp_meta_box), so on an ACF site you will not see it. In the classic editor it is under Screen Options.
Types only arrived at registration level: register_meta() in 4.6 (2016) with type, single, sanitize and auth callbacks; register_post_meta() in 4.9.8 (2018); array and object types over REST in 5.3; default values in 5.5; meta revisions only when you opt in with revisions_enabled, 6.4.
Even then the database stores a string. The type lives in the schema and the REST API, not in the table.
Sources: developer.wordpress.org/reference/functions/register_meta/ | make.wordpress.org/core/2018/07/27/registering-metadata-in-4-9-8/ | wptavern.com/wordpress-4-6-expands-register_meta-to-support-registration-of-meta-keys
Stamp, best before 2009: featured images arrived in 2.9 (12.2009) and took over the box's best-known job, post images.

### 13. How to use (prehistoric) custom fields

A fun aside, not a recommendation to build client sites on this box.
Path in 7.1: Options menu (three dots), Preferences, General tab, Advanced section, Custom fields, Show & Reload Page. Save first, the editor reloads. In the classic editor it is under Screen Options.
It only appears for post types that support custom-fields (posts and pages do by default).
Why you do not see it on an ACF site: ACF sets remove_wp_meta_box to true and calls remove_meta_box('postcustom') (includes/forms/form-post.php). Core then drops enableCustomFields and the Preferences modal leaves the toggle out. To get it back with ACF active: add_filter('acf/settings/remove_wp_meta_box', '__return_false');
ACF's own comment on it: "removes expensive SQL query". The box runs SELECT DISTINCT meta_key over the whole wp_postmeta table for its key dropdown (limit 30, postmeta_form_limit). On a big site that is slow. postmeta_form_keys (4.4) lets you hand it a fixed list and skip the query.
Not very useful nowadays:
- Registered meta does the job properly. register_post_meta() gives a key a type, a default, sanitising and REST access, and Block Bindings put it in the editor. The box knows none of that.
- It shows too much we don't need. Every meta key without an underscore from every plugin and import ends up in the list, and the key dropdown offers up to 30 keys from the whole site.
- Text only. One name, one value, a textarea. No types, no validation, no image picker. Keys are typed by hand, so Photo credit, photo_credit and Photo Credit are three different fields.
What it was good for back then: before featured images arrived in 2.9 (12.2009), themes read the post image URL from a custom field, often called image or thumbnail. Today it is mostly for peeking at what a plugin saved into a post without opening the database.
Since 2004: verified in the WordPress 1.2 Mingus source (released 22.5.2004, wordpress.org/news/2004/05/heres-the-beef/). wp-admin/edit-form-advanced.php has the Custom Fields fieldset, install.php creates wp_postmeta, get_post_custom() and the_meta() exist. The release post itself does not mention it.
Stamp, 100% dependency-free: true, no plugin involved. It is the talk's own promise, just on the worst possible tool for it. It isn't deprecated: only the_meta() is (@deprecated 6.0.2), the box and get_post_meta() are live core.
Sources: wordpress.org/documentation/article/assign-custom-fields/ | wp-admin/includes/meta-boxes.php, wp-admin/edit-form-blocks.php, wp-admin/includes/template.php (meta_form) in 7.1

### 14. Advanced Custom Fields since 2011

ACF's first commit was 28.3.2011 (Elliot Condon). It made custom fields usable: field types, a real UI, repeaters. But everything it adds is still a field: a value in wp_postmeta that a template prints.
Blocks changed the unit of content from a field to a block. That is the shift this talk is about.

### 15. We thought we did “the core way”

The funny part: I felt we did the core way, but we still used ACF. You lie to yourself that you do the core way, but with ACF it is not the core way. And you do not want to be purist or elitist. You want the thing that is fast to build and works for years. ACF was that. Until it wasn’t.

I have always liked the core way of WordPress. Traditional themes, starting with Automattic's Underscores (_s), and that is how air-light was born: an easy starting point for developers like me.
air-light is a starter theme and meant to be minimal. It still does not ship blocks, and that is on purpose. For a long time I saw blocks as a dependency too. (Some competitors have criticised air-light for not being a block theme. Possible hook for the Which kind of theme? / Why we chose the classic way slides.)
I soon noticed there are different ways of doing WordPress, before and after the block era, and it was difficult to keep things directed at the core. There is value in staying close to the core ways and not deviating from the path too much.

Facts, air-light git history:
- First commit 29.1.2016. README: "Theme is originally based on _s".
- 4.9.2020 "Add gutenberg custom blocks", a first native block try. 17.9.2020 "Remove leftover register_block_type()", gone 13 days later.
- 11.5.2021 "add hooks that register new block group and all our acf blocks": ACF blocks, not native.
- 28.2.2025 first real native block code. air-light 10.0.0 on 3.2.2026.
Source: github.com/digitoimistodude/air-light

### 16. So what’s the answer?

So if ACF is still just fields and some heavy weight you need to get rid of, what's the answer?
For years our answer was: Gutenberg for articles, ACF for everything else. In 2018 I didn't even have time to test Gutenberg properly.
When we finally went native in 2025, we thought we knew the answer. Blocks are React, so we code every block ourselves, in React, every option by hand.
GIF: Deep Thought, The Hitchhiker's Guide to the Galaxy (2005). The answer is 42, and it was just as useful.

### 17. We thought “native” meant React.js

Our actual route, with dates.
2017: we added the Classic Editor to our stack to prepare for Gutenberg. 2018 to 2020: Gutenberg only for articles, pages stayed ACF. 2021: ACF blocks became our standard (air-light 11.5.2021).
In 2018 WordPress was telling everyone to "learn JavaScript, deeply" (State of the Word 2015), and when WP 5.0 shipped on 6.12.2018, a custom block meant JavaScript with a build step. That is exactly why ACF Blocks (announced 15.10.2018, released in ACF 5.8, 5.2019), Block Lab and Lazy Blocks existed: PHP developers didn't want to write React. WP Tavern called ACF 5.8 "a great relief".
28.2.2025: our first native blocks in air-light, an image-content static block and a dynamic block draft. 13.5.2025 in Slack I already wrote "a custom block is the last resort", but the fourth level of that plan was still "a fully custom block in React".
The peak: one client site built from 2.2026 to 5.2026 has 23 custom blocks, 77 attributes, about 4,130 lines of JavaScript (3,000 of it in edit.js), 45 InspectorControls.
Our pricing blocks on dude.fi went through three versions: v1 and v2 had a TextControl or TextareaControl per field, which meant no rich text, no links in lists, lots of attribute code and bad UX. v3 moved to InnerBlocks.
Sources: wordpress.org/news/2018/12/bebo/ | advancedcustomfields.com/blog/acf-5-8-introducing-acf-blocks-for-gutenberg/ | wptavern.com/advanced-custom-fields-5-8-0-introduces-acf-blocks-a-php-framework-for-creating-gutenberg-blocks | wptavern.com/state-of-the-word-2015-javascript-and-api-driven-interfaces-are-the-future-of-wordpress
The result, on that site: most blocks already used InnerBlocks and RichText on the canvas, the sidebar held only settings. What hurt was markup coded into the blocks: a colleague, 21.5.2026, the pattern refused to create a version without buttons, because the buttons were in code. From 5.2026 that site moved to core Group plus patterns.
ACF Gutenberg blocks since 2021: before that, pages were built with ACF Flexible Content. First ACF blocks in client themes 2.2021 ("Creating acf blocks"), made the air-light standard 11.5.2021 ("register new block group and all our acf blocks").

### 18. And suddenly we were JS devs

I am a traditional WordPress guy. I come from the Underscores world, never got into Sage, Twig, Blade or other templating languages. PHP, HTML and CSS.
Then WordPress took a huge leap and moved to React.
Underscores launched 13.2.2012. Mullenweg announced dropping React on 14.9.2017 over the patents clause; Facebook relicensed React under MIT days later and Gutenberg stayed on React.
Sources: themeshaper.com/2012/02/13/introducing-the-underscores-theme/ | ma.tt/2017/09/on-react-and-wordpress/ | ma.tt/2017/09/facebook-dropping-patent-clause/
Learning React was not for nothing. It taught us how the WordPress block editor itself works: blocks, attributes, InnerBlocks, the data stores, why save() has to match what's in the database. Knowing that is what lets us use core properly now, and tell when a custom block is actually needed.

### 19. Media and text, coded by hand

This is what "native meant React" looked like: the same media and text block, coded by hand. Illustrative, but it is the shape of our 2025 to 2026 blocks.
Nine files. block.json declares an attribute for every option. edit.js wires a control for each one: heading level, media side, background colour, padding, RichText for the heading, MediaUpload for the image. save.js has to print exactly the same HTML that is in the database, or the editor marks the block invalid. Change the markup later and you write a deprecation (our pricing block carries deprecated v1 and v2).
Every one of these controls already ships with the core Media & Text block: media position, colours and spacing from block supports and theme.json, and any blocks you want inside it.
What went wrong for us: text fields in a sidebar lost bold, links and lists. Buttons coded into a block could not be removed in a pattern (a colleague, 21.5.2026: the pattern refused to create a version without buttons, because the buttons were in code). And we maintained forever what core maintains for free.
Sources: developer.wordpress.org/block-editor/reference-guides/block-api/block-edit-save/ (markup that doesn't match save() is marked invalid) | developer.wordpress.org/block-editor/reference-guides/block-api/block-deprecation/
Core Media & Text has existed since the very first block editor: added in Gutenberg 4.1 (PR #9416, 10.2018), shipped with WordPress 5.0 on 6.12.2018. Source: make.wordpress.org/test/2018/10/19/call-for-testing-gutenberg-4-1-pre-release/
Was it mature enough in 2018? As a block, yes: it shipped in WordPress 5.0 (6.12.2018) with media left or right, stacking on mobile and a background colour. What came later is what makes it on-brand without code:
- Block styles you can add to any block: register_block_style, WordPress 5.3 (11.2019).
- Colours through the shared block supports: Media & Text moved to the colour support flag in Gutenberg 7.9 (merged 30.3.2020, WordPress 5.5, 8.2020).
- theme.json, where palette, sizes and per-block styles live: WordPress 5.8 (7.2021).
- Spacing, typography and border supports on the block arrived over later releases; today it has colour, gradients, padding, margin, typography and border.
So from 2021 onwards, the block we kept rebuilding by hand in 2025 could be fully themed from theme.json.
Sources: make.wordpress.org/core/2019/09/24/new-block-apis-in-wordpress-5-3/ | github.com/WordPress/gutenberg/pull/21169 | make.wordpress.org/core/2021/06/25/introducing-theme-json-in-wordpress-5-8/

### 20. React is for WordPress core developers

React is how the editor is built, so it's for the people building WordPress core. It is not a requirement for building themes and blocks.
Facts:
- The editor: @wordpress/element "builds on top of React and provide a set of utilities to work with React components and React elements" (Block Editor Handbook, packages-element). The handbook explains why React was chosen to model blocks.
- Themes: a block theme is HTML block templates plus theme.json (Theme Handbook). Patterns, block styles and theme.json are markup and JSON, no JavaScript.
- Custom blocks: Learn WordPress (13.10.2024) shows "you can also develop blocks without using" JSX and @wordpress/scripts. The editor side is still JavaScript, just not necessarily React you write yourself.
- Front end: the Interactivity API (6.5) is directives plus a small store, no React.
Sources: developer.wordpress.org/block-editor/reference-guides/packages/packages-element/ | developer.wordpress.org/themes/getting-started/what-is-a-theme/ | learn.wordpress.org/lesson/developing-wordpress-blocks-without-jsx-or-a-build-process/

### 21. Where your content lives

Where things live. With ACF, four places: the field groups are set up by hand in wp-admin and stored in the database, ACF draws the forms, the theme's PHP templates print the fields with get_field(), and every value is its own row in wp_postmeta.
Lose the database and you lose the field groups. That is why ACF 5 (2014) added Local JSON: it copies every field group into an acf-json folder in the theme, so the definitions can live in git and sync between environments. It works, but it's a copy of something that really lives in the database.
Many of us found it odd to build fields in an admin view at all, so we reached for code: ACF's own acf_add_local_field_group(), or libraries like ACF Codifier (Geniem, 2017) that we met on inherited sites. They all sit on top of ACF, so you now depend on ACF and on the library keeping up with ACF. Even more dependency.
With core blocks there are three places and no plugin: the block and all its options ship with WordPress core, the look lives in theme.json in the theme, and the content is block markup in post_content. There are no field groups to set up. The block's "fields" are the block.
Sources: advancedcustomfields.com/resources/local-json/ (saves field groups as JSON in the theme, "allows for version control over your field settings") | github.com/devgeniem/acf-codifier (created 17.9.2017)

### 22. True dependency-free WordPress is the core way

Jokes aside. Dependency-free here means no plugin dependency when it comes to content: WordPress itself is still the one dependency we choose on purpose, as on the definition slide.
The rest of the talk is how we got there from ten years of ACF.

### 23. Three ways to build a sovereign theme

I am a traditional WordPress guy. I come from the Underscores world and never got into Sage, Twig, Blade or other theme frameworks and templating languages. I stuck to PHP, HTML and CSS, and I am a fan of the core way. It avoids vendor lock and it feels nice to be able to do things like core intended.

Traditional: Underscores (_s), Automattic, launched 13.2.2012. Classic PHP templates following the template hierarchy.
Innovative: Sage by Roots, started as the Roots theme in 2011. Sage 11 (2025) runs onAcorn with Laravel Blade views in resources/views, Composer, and Vite as the build tool.
Modern: block themes arrived with WordPress 5.9 in January 2022. HTML templates and parts, theme.json for settings and styles, edited in the Site Editor.
Sources: themeshaper.com/2012/02/13/introducing-the-underscores-theme/ | roots.io/sage-v11-and-acorn-v5-released/ | make.wordpress.org/core/2021/06/25/introducing-theme-json-in-wordpress-5-8/

### 24. From Traditional to Modern

How to get from a traditional theme with ACF to a modern one. You do not have to jump in one go: every step on the stairs works inside a classic theme, which is what a hybrid theme is.
1 Native blocks (5.0+, block.json canonical in 5.8): replace ACF blocks with core blocks, patterns and your own blocks. Content first, theme untouched.
2 Post meta (Block Bindings 6.5+, editing bound values 6.7, custom sources UI 6.9): register_post_meta() instead of ACF fields, bound to core blocks.
3 theme.json (5.8+): settings and styles in a classic theme. A classic theme with theme.json or editor-styles gets Appearance > Design (Style Book) instead of just Patterns (wp-admin/menu.php in 7.1).
4 Block template parts (6.1+): add_theme_support('block-template-parts') plus a /parts folder, header and footer editable as blocks (@since 6.1.0 in wp-includes/theme.php).
Last step, Modern: block theme with /templates HTML templates, detected by wp_is_block_theme() (5.9, January 2022), full site editing.
Panel extras: WP REST API is on the Traditional side on purpose, core since 4.7 (12.2016) and it works in any theme. Interactivity API: core since 6.5 (3.2024), front-end behaviour through directives in block markup. AI client: wp_ai_client_prompt() @since 7.0.0, on top of the Abilities API @since 6.9.0. If asked: the AI client and Abilities API work with a classic theme too, they are modern core, not block-theme-only.
Is full site editing worth it? It depends on who edits what:
- For: one design system in theme.json, no PHP templates, the client can edit headers, footers and templates in the Site Editor, and it is where core is going.
- Against: templates edited in the Site Editor are saved to the database and drift from the theme files in git, clients can change layouts you wanted locked, and the tooling and docs still move between releases.
- Adoption, June 2026: block themes are 13% of the 14,822 wordpress.org themes and 44% of new submissions, but only 8.3% of non-default theme installs; classic themes still win about 11:1 (wp.md/blog/state-of-wordpress-themes-2026/, install counts are wordpress.org buckets).
- Hybrid is a valid place to stop, not only a stop on the way.
Sources: developer.wordpress.org/news/2024/12/bridging-the-gap-hybrid-themes/ (Troy Chaplin, 3.12.2024; it dates block template parts to 5.9, core says 6.1 for classic themes) | learn.wordpress.org/lesson/converting-a-classic-theme-to-a-block-theme/ | developer.wordpress.org/themes/

### 25. Why go 100% core

So if you're still on ACF, why go 100% core for your blocks?

First, performance. A lot of the work moves from the server to the browser, and the page itself is just saved block markup.

Second, the basics are built in. Heading levels, colours, spacing. With ACF we had to build every one of those settings by hand. Even changing an h1 to an h2 was a job for a developer. And the WYSIWYG field was a pain: our editors couldn't even put bold text or a link in the middle of a sentence the way they wanted.

Third, the client edits right in the preview. No more jumping between an edit view and a preview view. Our big ACF blocks used to flicker every time you touched them.

Fourth, you get Lego and Duplo at the same time. Big ready-made pieces and small ones, mixed however you like. And anything can be moved, reordered and combined.

And the client gets a real tool. A few years ago one of our clients emailed us that he was about to lose his mind in "the WordPress straitjacket Dude knitted". He was half joking, but the name stuck with us.

The cons. There is a steep learning curve, for the whole team. You write less PHP and more JSON, theme.json and block.json, which is new ground for a lot of CSS developers. You have to unlearn the habit of building every block from scratch and start from what core already has. When you do need a custom block, you get the heavy build tooling: React, npm, a build step. And core moves fast while the docs are scattered.

When we started, I said this would take our team a year or more to absorb. It's wonderful and horrible at the same time. The designer side of it is on the next slide.

(Sources, not to read out: the straitjacket email 7.11.2023; the flicker comment in our developer channel 11.9.2024; "a year or more" 17.4.2026; "wonderful and horrible" voicenote 29.4.2026.)

### 26. The designer’s new job

Before, designers used to limit what the customer can do. Now we give complete freedom. We need to design all blocks so that they look like the customer's brand. With great power comes great responsibility.
Practical side: the design system goes into theme.json (palette, font sizes, spacing scale), block styles and patterns, so the choices the client can make are all on-brand. Lock what must not change with templateLock and block locking, curate with allowed blocks.

Evidence: Dude's designer carousel "Natiivilohkot suunnittelijan näkökulmasta" (6.2026): "Jos asiakkaalle annetaan vapaasti käyttöön 14 fonttikokoa... sivusto alkaa muistuttaa kollaasia" (give the client 14 font sizes freely and the site starts to look like a collage). A designer in the 23.2.2026 session: "asiakas ei pääse ehkä liikaa siellä myllertämään?" Answer: curate in theme.json, MAYBE fewer choices, all on brand. But we’ve decided to give as much as choices as possible and make them look good in all scenarios.

### 28. Ways to build a block

21 ways to build a block, and that is the point: this is why moving off ACF feels confusing. You do not need all of them.
Column 1, no custom code: core blocks, variations, patterns, styles, filters, and synced patterns (reusable blocks, renamed synced patterns in 6.3; pattern overrides in 6.6).
Column 2, your own code: register_block_type / registerBlockType, block.json, dynamic render.php, React, InnerBlocks, and interactive blocks with the Interactivity API (core since 6.5).
Column 3, the in-betweens and third parties: ACF blocks, hybrid setups, theme choices, Block Bindings, and page builders like Elementor and Divi, which bring their own editor and their own content format. Elementor keeps the layout as JSON in post meta (_elementor_data), so the content only makes sense with the plugin active. The same dependency problem as ACF, just bigger.

### 29. From core to custom, prioritized

Priority order: reach for 1 before 2, 2 before 3, and write a custom block only when nothing above fits.
Order of preference in our converter spec: core blocks as a pattern first, a custom native block only for queries, external APIs or interactive widgets, and a hybrid wrapper with InnerBlocks in between.
The 115 block count is WordPress 7.1's core inventory as recorded in our converter spec (DEV-1056).

### 30. Block example: Media and text

Same block, two ways. Left: the image and text block on our most recent ACF site to launch (5.2026), anonymised. The editor fills a fixed form: title, one WYSIWYG box, one link, one image. The PHP template decides the markup and the content lives in ACF fields. No second button, no list, no video, and every new variation means a developer adds a field.
Right: priority 1, a core block as shipped. core/media-text has been in core since WordPress 5.0. There is nothing to build: no PHP, no JS, no field group. This is what the editor saves into post_content (trimmed: the real markup also has is-stacked-on-mobile and the image classes). Inside the content half the client can use any blocks: heading, paragraph, buttons, lists, whatever.
Styling comes from theme.json and a block style if needed (priority 3). Wrap the markup in a pattern file to give editors a ready-made starting point (priority 2).
Our latest native site did this one as a small custom block around core blocks. For this layout core/media-text would have done the job, which is the point of the priority order.
Core Media & Text has existed since the very first block editor: added in Gutenberg 4.1 (PR #9416, 10.2018), shipped with WordPress 5.0 on 6.12.2018. Source: make.wordpress.org/test/2018/10/19/call-for-testing-gutenberg-4-1-pre-release/

### 31. Most of the time you don’t need to code a block

The Media & Text example on the previous slide is the typical case: the ACF version was a field group plus a PHP template, the core version is a block that already exists. Search the inserter first.
115 core blocks is WordPress 7.1's inventory as recorded in our converter spec (DEV-1056).
Proof from our own work: one of our 2026 sites (6.2026) was built with zero custom blocks. Core blocks, three block styles (gallery marquee and masonry, a gradient button), theme.json styling and patterns. That is all.

### 32. When you do code: the Dude House Way

Most of the time you don't need to code. But when you do, this is how we do it at Dude today.

1. We lock theme.json first. A fixed palette, a named type scale, a fluid spacing scale, fixed content widths. Custom colours, custom sizes, line height, drop caps: all off. The client picks from our scale and never types a value. This is the brand guard from the designer slide.

2. Core blocks by default, and we curate them per post type. A news post doesn't need the same blocks as a landing page. We also remove the bundled core and WooCommerce patterns and most of the embed providers, so the inserter only shows what fits the site.

3. We style core blocks and their variations in theme.json. SCSS only for what theme.json can't do. The style names are registered in PHP so they show up in the editor's Styles panel, but the look lives in theme.json.

4. Layouts are patterns built from core blocks, in the editor. We have actually deleted custom blocks that turned out to be only layout and rebuilt them as patterns. A pattern is a starting point the client can change; a custom block is code we maintain forever.

5. Public data comes from the WP REST API and is rendered in the browser. We try to avoid render.php. No PHP rendering per block, no server round trip just to show a preview in the editor, and the same endpoints serve the site, the editor and anything else.

6. When a block has to react without a page reload, filters, sorting, paging, we use the Interactivity API. It has been in core since 6.5. You write directives in the markup, data-wp-on--click, data-wp-text, data-wp-each, and a small store in view.js. No React on the front end, no build step for the front-end script.

7. And only then, as the last resort, a custom block. Few attributes, narrow supports, block.json with a view.js, built with wp-scripts. That's the folder on the right.

ACF is still installed on these sites, but it builds no blocks. It's a form builder for data: custom post type fields, menu flags, settings screens. For plain text fields on a simple marketing site we don't even need ACF, a registered meta field is enough.

If asked about render.php: some of our current blocks still use it. That is exactly what we are moving away from for public data.

### 33. Site Editing/Block theme: our first build

Our first full site editing build: a small route guide site, 5.2026 to 6.2026, converted from air-light into a block theme. How it is built: templates/ has index, page, page-no-sidebar and 404; parts/ has header and footer. theme.json v3 declares templateParts and customTemplates, loads the font with fontFace, and turns off custom colours, sizes, line height, letter spacing, borders and shadows. Four patterns live in patterns/*.php under our own category; core and remote patterns are unregistered.
No custom blocks, no ACF, no Interactivity API. Small vanilla JS fills the gaps: the sidebar navigation accordion and a print button. Editors change header, footer and menus in the Site Editor, reached from a "Muokkaa sivustoa" admin link. The header groups are locked against moving and removing.
The honest lessons:
- Git and the database drift. Templates were built in the local Site Editor and pasted into files, so they carry database IDs (navigation ref, image ids) and local URLs. Any edit in the Site Editor on production creates a database copy that overrides the file, and nothing brings it back to git. Decide up front who owns templates, and use an export workflow (for example the Create Block Theme plugin) if files are the source of truth.
- Core Navigation is not built for a sidebar menu: "Tuo coren nav ei oikein palvele kunnolla tossa sivupalkissa, kun ei ole siihen tarkoitettu" (our project channel, 3.6.2026). Solved with custom JS and SCSS.
- Converting a classic starter leaves dead code: nav walkers and CSS that fought theme.json had to be removed by hand.
- Multilingual was hard: Polylang only swaps a navigation ref when templates are duplicated, not for a shared template. It was added and removed again.
The upside: almost no custom code, the design options come from theme.json, and editors manage header, footer and menus without a developer.

### 34. Fields outside blocks, without ACF

Everything so far was page content. But people also build custom post types with fields, and archive pages. How without ACF?
The post type: register_post_type() in the theme or a small plugin. Core since 3.0 (2010).
Its fields: register_post_meta() with a type, a default and show_in_rest. Arrays and objects work too (5.3). Show the value with a Block Binding: a core heading, paragraph, image or button reads it and the editor edits it in place (6.5, editable since 6.7).
Single and archive pages: a template, PHP in a classic theme or HTML in a block theme, with the Query Loop block for the listing. Sorting or filtering by a meta field, like upcoming events by date, needs a small hook (query_loop_block_query_vars, 6.1) or a custom block.
Complex fields and settings: this is where ACF still earns its place. Core can store a repeater or a relationship, but has no editing UI for them, and bindings only take simple values. Same for site-wide options pages. Our team still uses ACF exactly for this on our 2026 sites, and reads it with get_post_meta().
If asked about FSE: it makes the templates editable, it doesn't add fields.

### 35. This is a lot, where to start, going 100% ACF-free?

That's a lot of new things. If you only take one of them home, take patterns. They need no code, they work in every theme, classic or block, and they are the fastest way to get away from ACF blocks.

### 36. It has always been a pattern

It has always been a pattern. When we went through the 49 ACF blocks of one client site, 32 of them only printed layout and typed copy: headings, text, images, cards. Every one of those was a pattern all along, we just built it as a block.
A pattern is nothing more than core blocks arranged once and saved. No code, no build step. The client inserts it and can change anything in it, because it isn't locked in code.
Patterns have been in core since WordPress 5.5 (8.2020). Synced patterns, the old reusable blocks, since 6.3 (8.2023), and pattern overrides since 6.6 let one synced pattern have per-page content.
Sources: make.wordpress.org/core/2020/07/16/block-patterns-in-wordpress-5-5/ | our own conversion analysis of a client site, 9.2026.

### 37. Start every page from a pattern

New from the last weeks. When a client creates a new empty page, the editor opens on a blank canvas. Blocks alone don't show how to build a whole section, and clients who never open the Patterns tab don't know the finished sections exist.
WordPress already has a "Choose a pattern" window for new pages, but it only lists patterns registered with blockTypes core/post-content. Patterns people save in the editor never carry that, so on our sites the window never opens.
Left: the core way, for patterns in theme files. Right: what we do for editor-saved patterns. On a new, empty page we open the inserter on the Patterns tab. It uses core's own "All" string, so it's already translated.
It's coming to air-helper, our open source helper plugin, on by default, with a filter to turn it off: add_filter( 'air_helper_enable_page_patterns_onboarding', '__return_false' ).
Caveat if asked: tab and category map to __experimental props in core, so we recheck on every major release.

### 38. What does it look like?

This is what the client sees on a new, empty page: the editor opens with the Patterns tab (Mallit) already open, and the finished sections are right there, contact form, logo wall, text and media, columns with icons, hero. Drag one in and edit it.
Screenshot: our demo site with the air-helper change turned on.

### 39. Learning this with your AI

AI is great for learning this, with one caution. Because there are so many ways to build a block and the docs are scattered, AI makes the same mistakes we did. Ask it for a block and it often writes a full hand-coded React block: that's the most common answer in its training data, it's too lazy to look for the core way, or we're too lazy to prompt properly, or it simply doesn't find the right documentation.
So tell it the priority order up front: core blocks, then patterns, then block styles, and a custom block only as the last resort. The prompt on the next slide does exactly that.
Make it show the handbook page it based the answer on, and review the code like you'd review a colleague's.

### 40. When ACF still makes sense

So, ditch ACF completely? Not always. This is where ACF is still the more sensible choice.
Integrations: a lot of the plugin ecosystem reads ACF fields directly. Translation plugins like Polylang, search like FacetWP or Relevanssi, SEO plugins. Replacing ACF there can mean rebuilding the integration too.
Settings pages: an ACF options page is a few lines. In core it's the Settings API and a form you write yourself.
Relationships: "these posts belong to this one" with a nice picker. Core stores it fine, but has no editing UI. A taxonomy covers some cases, not all.
Where blocks get in the way: structured data that isn't page content. Product specs, opening hours, event dates with validation. Those want a form with fields, not a canvas of blocks.
So the rule is: pages and layout with core blocks and patterns, structured data with whatever makes the form easiest. Often that's still ACF, and that's fine.
