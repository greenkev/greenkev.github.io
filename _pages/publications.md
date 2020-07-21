---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: true
---

{% if author.googlescholar %}
  You can also find my articles on <u><a href="{{author.googlescholar}}">my Google Scholar profile</a>.</u>
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
