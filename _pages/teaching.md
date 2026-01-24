---
layout: page
permalink: /teaching/
title: teaching
description: Materials for courses
nav: true
nav_order: 5
---

<div class="projects">
  {% assign sorted_projects = site.teaching | sort: "importance" %}

  {% if page.horizontal %}
    <div class="container">
      <div class="row row-cols-1 row-cols-md-2">
        {% for project in sorted_projects %}
          {% include projects_horizontal.liquid %}
        {% endfor %}
      </div>
    </div>
  {% else %}
    <div class="row row-cols-1 row-cols-md-3">
      {% for project in sorted_projects %}
        {% include projects.liquid %}
      {% endfor %}
    </div>
  {% endif %}

</div>

### Image attribution

PHYS 7221, Fall 2023: "<a target="_blank" rel="noopener noreferrer" href="https://www.flickr.com/photos/49681564@N06/18240342073">Arthur Tombs and Quang Ha: Double Pendulum 1</a>" by <a target="_blank" rel="noopener noreferrer" href="https://www.flickr.com/photos/49681564@N06">Engineering at Cambridge</a> is licensed under <a target="_blank" rel="noopener noreferrer" href="https://creativecommons.org/licenses/by-nd-nc/2.0/jp/?ref=openverse">CC BY-NC-ND 2.0 <img src="https://mirrors.creativecommons.org/presskit/icons/cc.svg" style="height: 1em; margin-right: 0.125em; display: inline;"><img src="https://mirrors.creativecommons.org/presskit/icons/by.svg" style="height: 1em; margin-right: 0.125em; display: inline;"><img src="https://mirrors.creativecommons.org/presskit/icons/nc.svg" style="height: 1em; margin-right: 0.125em; display: inline;"><img src="https://mirrors.creativecommons.org/presskit/icons/nd.svg" style="height: 1em; margin-right: 0.125em; display: inline;"></a>. 

PHYS 7364, Spring 2022: <a href="https://www.flickr.com/photos/35734278@N05/15693117819">"Newly discovered superconductor state opens a window to the evolution of the universe"</a><span> by <a href="https://www.flickr.com/photos/35734278@N05">Argonne National Laboratory</a></span> is licensed under <a href="https://creativecommons.org/licenses/by-nc-sa/2.0/?ref=openverse&atype=html" style="margin-right: 5px;">CC BY-NC-SA 2.0</a><a href="https://creativecommons.org/licenses/by-nc-sa/2.0/?ref=openverse&atype=html" target="_blank" rel="noopener noreferrer" style="display: inline-block;white-space: none;margin-top: 2px;margin-left: 3px;height: 22px !important;"><img style="height: inherit;margin-right: 3px;display: inline-block;" src="https://search.creativecommons.org/static/img/cc_icon.svg?image_id=f4868a2f-21f0-41e2-83f2-a4a4cc376c17" /><img style="height: inherit;margin-right: 3px;display: inline-block;" src="https://search.creativecommons.org/static/img/cc-by_icon.svg" /><img style="height: inherit;margin-right: 3px;display: inline-block;" src="https://search.creativecommons.org/static/img/cc-nc_icon.svg" /><img style="height: inherit;margin-right: 3px;display: inline-block;" src="https://search.creativecommons.org/static/img/cc-sa_icon.svg" /></a>