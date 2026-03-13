---
layout: page
permalink: /talks/
title: talks
description: talks, seminars, and conference presentations
nav: true
nav_order: 3
---

<div class="projects">
  {% assign sorted_talks = site.talks | sort: "date" | reverse %}
  <div class="row row-cols-1 row-cols-md-3">
    {% for project in sorted_talks %}
      {% include projects.liquid %}
    {% endfor %}
  </div>
</div>
