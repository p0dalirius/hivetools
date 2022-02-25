# Hivetools

<p align="center">
   A collection of python scripts to work with Windows Hives.
   <br>
   <img src="https://badges.pufler.dev/visits/p0dalirius/hivetools/"/>
   <img alt="GitHub release (latest by date)" src="https://img.shields.io/github/v/release/p0dalirius/hivetools">
   <a href="https://twitter.com/intent/follow?screen_name=podalirius_" title="Follow"><img src="https://img.shields.io/twitter/follow/podalirius_?label=Podalirius&style=social"></a>
  <br>
</p>

![](./.github/json.png)

## Examples

 + Get a specific key in a hive:

    ```
    ./hive-get-keys.py -H ./examples/hives/SAM -k 'SAM\Domains\Builtin\Aliases\Members\S-1-5-21-877132822-430060850-1589397531\000001F4\(default)'
    ```

 + Exporting a hive to JSON:

    ```
    ./hive-to-json.py --hive ./examples/hives/SYSTEM -o ./examples/json/SYSTEM.json
    ```

## Contributing

Pull requests are welcome. Feel free to open an issue if you want to add other features.

## References
 - http://sentinelchicken.com/data/TheWindowsNTRegistryFileFormat.pdf
 - https://github.com/msuhanov/regf/blob/master/Windows%20registry%20file%20format%20specification.md
