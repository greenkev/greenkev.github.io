---
layout: archive
title: "Personal Projects"
permalink: /personal_projects/
author_profile: true
---

{% include base_path %}


{% for post in site.personal_projects reversed %}
  {% include archive-single.html%}
{% endfor %}

