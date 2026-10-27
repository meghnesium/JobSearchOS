# Run the filename check every Friday (any AI tool, no AI cost)

Replace `/path/to/your/folder` and the script path.

## macOS (launchd)

Save as `~/Library/LaunchAgents/com.jobsearchos.sync.plist`, then `launchctl load ~/Library/LaunchAgents/com.jobsearchos.sync.plist`:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0"><dict>
  <key>Label</key><string>com.jobsearchos.sync</string>
  <key>ProgramArguments</key><array>
    <string>/usr/bin/python3</string>
    <string>/path/to/sync-filenames.py</string>
    <string>/path/to/your/folder</string>
    <string>--apply</string>
  </array>
  <key>StartCalendarInterval</key><dict>
    <key>Weekday</key><integer>5</integer>
    <key>Hour</key><integer>15</integer>
    <key>Minute</key><integer>0</integer>
  </dict>
  <key>StandardOutPath</key><string>/path/to/your/folder/logs/sync.log</string>
  <key>StandardErrorPath</key><string>/path/to/your/folder/logs/sync.log</string>
</dict></plist>
```

## Linux or macOS (cron)

`crontab -e`, then add:

```
0 15 * * 5 /usr/bin/python3 /path/to/sync-filenames.py /path/to/your/folder --apply >> /path/to/your/folder/logs/sync.log 2>&1
```

## Windows (Task Scheduler)

Create a Basic Task, trigger Weekly on Friday, action Start a program:

- Program: `python`
- Arguments: `C:\path\to\sync-filenames.py "C:\path\to\your\folder" --apply`

If the computer is asleep on Friday, the run happens at next wake on most systems. You can always run it by hand without `--apply` first to see what it would change.
