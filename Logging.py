import datetime

formatted_time = lambda timezone, format: datetime.datetime.now(tz=timezone).strftime(format)

class Logger:

  def __init__(self, fileName: str, echo: bool = False) -> None:
    self.fileName = fileName
    self.echo = echo

  def log(self, event: str, level: str, message: str):
    with open(file=self.fileName, mode='a+') as file:
      output = "[{prefix}] <{event}> ({level}) : {message}".format(prefix=formatted_time(datetime.timezone.utc, "%Y-%m-%d %H:%M:%S.%f"), event=event, level=level, message=message)
      file.write(output + '\n')
      if self.echo: print(output)

if __name__ == '__main__':
  LoggerTester = Logger(fileName="LoggerTester.log")
  LoggerTester.log(event="LoggerTester", level="Information", message="Testing Logger")