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
  {%if post.publication_type == 'inbook'%}
<h2 class="archive__item-title"> Book Chapters </h2>
    {% break %}
  {% endif %}
{% endfor %}
{% for post in site.publications reversed %}
  {%if post.publication_type == 'inbook'%}
    {% include archive-single-publication.html %}
  {% endif %}
{% endfor %}


<h2 class="archive__item-title"> Peer-Reviewed Journal Papers </h2>

{% for post in site.publications reversed %}
  {%if post.publication_type == 'article'%}
    {% include archive-single-publication.html %}
  {% endif %}
{% endfor %}

<h2 class="archive__item-title"> Peer-Reviewed Conference Papers </h2>

{% for post in site.publications reversed %}
  {%if post.publication_type == 'inproceedings'%}
    {% include archive-single-publication.html %}
  {% endif %}
{% endfor %}

<h2 class="archive__item-title"> Patents </h2>

{% for post in site.publications reversed %}
  {%if post.publication_type == 'patent' %}
    {% include archive-single-publication.html %}
  {% endif %}
{% endfor %}
