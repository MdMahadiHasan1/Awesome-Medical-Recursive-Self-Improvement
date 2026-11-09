# Contributing

We welcome primary-source corrections, stronger evidence notes, and additions that explain how a resource helps study self-improving medical or biomedical AI.

1. Search the [paper catalog](docs/papers.md) and [benchmark guide](docs/benchmarks.md) by title, acronym, DOI, and arXiv ID. Update the existing entry when a preprint is published. Use an internal link when a work also belongs in another category.
2. Open a [paper or resource suggestion](https://github.com/MdMahadiHasan1/Awesome-Medical-Recursive-Self-Improvement/issues/new?template=resource.yml) or submit a pull request. Include the primary source, venue or preprint status, and the update target, feedback source, and evaluation setting when the paper reports them.
3. Place the paper in one primary section using the [classification guide](docs/taxonomy.md). Use short, original notes. Add optional code and data links from the authors or official project, and use the published venue and year when available.
4. Run `python3 scripts/check_catalog.py` before opening a pull request. It checks duplicate paper links and relative documentation links. Open the primary and optional artifact links manually to verify that they point to the intended records.

Use this format in the paper catalog.

```markdown
- [Paper title](https://example.org/paper) · Venue, Year · **Persistent**. Name what is updated, the feedback used, and what is evaluated. [Code](https://example.org/code)
```

For a dataset or environment, state what it measures, how access works when documented, and whether it provides training feedback, evaluation, or both. Report a size only when the source identifies the relevant version or split. For corrections, include the affected entry and the source supporting the change.

Please keep discussion focused on the work. Use public research examples and avoid sharing patient records, identifiers, private credentials, or restricted datasets in issues and pull requests.
