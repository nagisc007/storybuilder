# ChangeLog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/en/1.0.0/)
and this project adheres to [Semantic Versioning](http://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.0.4] - 2019-03-19
### Added
- ActionGroup class
- Master class (inherited Subject class)
### Changed
- Action class < Act class
- Story management as ActionGroup
### Deleted
- Story class
- Episode class
- Scene class

## [0.0.3] - 2019-03-18
### Added
- Github issue template
- Github pull request template
- BaseAction class
- Story class
- Episode class
- Scene class
- story building method
- option parser
- output as action infos
### Changed
- Act's verb without a particle
### Fixed
- Failed to equal sentences in testtools

## [0.0.2] - 2019-03-11
### Added
- Act class to add a new attr "behavior"
- Behavior enum types (from major english verbs)
- Subject class for using act's subject base
### Changed
- Person, Stage, Item and DayTime class based Subject
- Story check test completely 5w1h.
### Deleted
- Example story and test.
- ActType(MUST, DONE)
- Must and Done act (instead to an act behavior).

## [0.0.1] - 2019-03-08
### Added
- This CHANGELOG file to hopefully serve as an evolving example of a standardized open source project CHANGELOG.
- README one line implemented.
- Basic classes to build a story.
- Test suites for basic features.
- Example story as usage.
- Output story as markdown.

[Unreleased]: https://github.com/nagisc007/storybuilder/compare/v0.0.4...HEAD
[0.0.4]: https://github.com/nagisc007/storybuilder/releases/v0.0.4
[0.0.3]: https://github.com/nagisc007/storybuilder/releases/v0.0.3
[0.0.2]: https://github.com/nagisc007/storybuilder/releases/v0.0.2
[0.0.1]: https://github.com/nagisc007/storybuilder/releases/v0.0.1
