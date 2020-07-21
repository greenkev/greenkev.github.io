---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: true
---

{% if site.author.googlescholar %}
  <div class="wordwrap">You can also find my articles on <a href="{{site.author.googlescholar}}">my Google Scholar profile</a>.</div>
{% endif %}

{% include base_path %}



{% for post in site.publications reversed %}
  {%if post.publication_type == 'inproceedings' or post.publication_type == 'article'%}
    {% include archive-single.html %}
  {% endif %}
{% endfor %}

<h1> Patents </h1>

{% for post in site.publications reversed %}
  {%if post.publication_type == 'patent' %}
    {% include archive-single.html %}
  {% endif %}
{% endfor %}
