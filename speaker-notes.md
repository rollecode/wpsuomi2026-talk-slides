# Speaker notes, raw

Rolle's thoughts as sent, kept verbatim-ish so nothing is lost before it
lands on a slide. The per-slide notes in talk.py are distilled from here.

## 24.9.2026, the history arc (slides 3 onwards)

- Slide 3: "A brief history of fields and dependencies in WordPress". Look a
  bit back.
- I used to do WordPress with meta fields only, when it was only about
  blogging. Works fine for a developer, it's kind of like knifing the
  database field directly. But if the customer wants to update content
  easily, you need a system.
- There were things like CMB2 and Carbon Fields, but we quickly settled on
  ACF, as it was the "industry standard" in a sense, and WordPress had no
  nice and fast way to add your own custom fields without custom code.
- Other dependencies too. WordPress works fine without plugins, and for
  purists like me the fewer plugins the better. Third-party code is always a
  liability (doesn't count my own plugins, throw a joke here) and makes sites
  slower unless you audit each plugin carefully, e.g. no endless queries that
  hit the database on every single load.
- So fewer dependencies is a good thing. But Gutenberg complicated it.
  Suddenly an npm package for block scripts (@wordpress/scripts), blocks in
  the theme, as a plugin, many blocks in one plugin, in theme AND plugin,
  registered via JS or PHP or both, or built in wp-admin only, and so on.
- Suddenly we had no idea how to build blocks, but we knew the native way was
  the only way.
- I'm a "traditional" WordPress guy. I come from the Underscores world, never
  got into Sage, Twig, Blade or other theme frameworks or templating
  languages. Stuck to PHP, HTML and CSS.
- Slide idea: "And suddenly we were JS developers", WordPress took a huge
  leap and moved to React.
