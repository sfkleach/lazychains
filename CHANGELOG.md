# Change Log for Lazychains Project

Following the style in https://keepachangelog.com/en/1.0.0/

## [0.2.9] Updates poetry.lock following vulnerability alert, 2023-10-20

### Changed

- poetry.lock

## [0.2.9] Updates poetry.lock following vulnerability alert, 2023-10-03

### Changed

- poetry.lock

## [0.2.8] Updates poetry.lock following vulnerability alert, 2023-08-19

### Changed

- poetry.lock

## [0.2.7] Updates development packages following vulnerability alert, 2023-05-24

### Changed

- Versions of mypy, sphinx and pytest updated to latest.


## [0.2.6] Fixes type hint, 2023-02-03

### Added

- mypy added

### Fixed

- Type hints

## [0.2.4] Bug fix for len_is_more_than, 2023-02-12

### Added

- Reasonable coverage of unit tests

### Fixed

- `len_is_more_than` method referenced an undefined variable.


## [0.2.4] Bug fix for expanded_len, 2023-02-12

### Fixed

- `expanded_len` method did not correctly handle fully expanded chains.


## [0.2.3] Lazycall and New Methods, 2023-02-03

### Added

- `lazycall` method and top-level calls implemented for implementing lazy functions that deliver chains.
- `map`, `filter` and `zip` methods added that have identical parameters to the built-ins, except they returns chains, as you might expect.
- Negative indexes have been implemented for `__getitem__`.
- New `dest` method added - returns the head and tail at the same time.
- New `expanded_len` method added to support teaching and debugging.

### Changed

- Test methods slightly extended.
- Documentation expanded with the maze example.
- Backfilled CHANGELOG.md.

## [0.1.3] Tidy up, 2023-01-30

### Changes

- Improved error message in `__getitem__`.
- Improved code comments.
- Added a few more tests.

## [0.1.2] Bug Fixes, 2023-01-29

### Fixed 

- Bug in negative indexing fixed.
