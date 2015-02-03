# Tarbell

Tarbell makes it simple to put your work on the web, whether you’re a team of one or a dozen. With Tarbell, you can collaboratively build beautiful websites and publish them with ease.

Tarbell makes use of familiar, flexible tools to take the magic (and frustration) out of publishing to the web. Google spreadsheets handle content management, so changes to your stories are easy to make without touching a line of code. Step-by-step prompts help you set up and configure your project, so that publishing it is a breeze.

The most recent version of Tarbell is 1.0 (released Dec. 8, 2014).

## Resources

* [**Install Tarbell**](http://tarbell.readthedocs.org/en/1.0/install.html) | [Tutorial](http://tarbell.readthedocs.org/en/1.0/tutorial.html) | [Documentation](http://tarbell.readthedocs.org)
* [**File an issue**](https://github.com/tarbell-project/tarbell/issues) | [Source code](https://github.com/tarbell-project/tarbell/)
* [**Follow on Twitter @tarbellproject**](https://twitter.com/tarbellproject) 

Tarbell was created by the [Chicago Tribune News Applications Team](http://apps.chicagotribune.com)
and is maintained by her contributors.


## Adding showcase projects:

1. Fork the repo
2. Add a post under `_showcase`. Make sure it has the necessary fields (see below)
3. Send a pull request


### Showcase post format

Posts are written in Markdown using YAML Frontmatter. Here's a complete example:

    ---
    title: Crime and Punishment in Chicago
    link: http://crime-punishment.smartchicagoapps.org/
    repo: https://github.com/sc3/crime-punishment
    spreadsheet: <link to project spreadsheet>
    date: "July 18, 2014"
    credit: Smart Chicago Collaborative
    ---

    Crime and Punishment in Chicago is an index of data sources surrounding this 
    criminal justice system as it is in Chicago. We track data sources from the 
    commission of the crime all the way to prison. We aggregate sources of data, 
    provide insight into how this data is generated, discuss how to get it, and 
    expose what data is unavailable.

The only required fields are `title`, `date` and `link`. If the project doesn't have an obvious publish date, just use the date you're adding the project here.
