# My_URL_Shortner
A fast and efficient URL shoortner made in python that can  able to store a lot of links
## Design Goals
Here's what we came up with:

1. We should be able to store a lot of links, since we're not automatically expiring them.
2. Our shortlinks should be as short as possible. The whole point of a link shortener is to make short links! Having shorter      links than our competition could be a business advantage.
3. Following a shortlink should be fast.
4. The shortlink follower should be resilient to load spikes. One of our links might be the top story on Reddit.

## Data Model
Let's call our main entity a Link. A Link is a mapping between a short_link on our site, and a long_link, where we redirect people when they visit the short_link.
Link
- short_link
- long_link
The short_link could be one we've randomly generated, or one a user chose.
Of course, we don't need to store the full ShortLink URL (e.g. bit.ly/mysite), we just need to store the "slug"—the part at the end (e.g. "mysite").

## Using base conversion to generate slugs
We usually use base-10 numbers, which allow 10 possible numerals: 0, 1, 2, 3, 4, 5, 6, 7, 8, and 9.
Binary is base-2 and has 2 possible numerals: 0 and 1.
Our random slug alphabet has 62 possible numerals (A-Z, a-z, and 0-9). So we can think of each of our possible "random" slugs as a unique number, expressed in base-62.





Okay, now our redirects should go pretty quick, and should be resilient to load spikes. We have a solid system that fits all of our design goals!

1. We can store a lot of links.
2. Our shortlinks are as short as possible.
3. Following a shortlink is fast.
4. The shortlink follower is resilient to load spikes.
