#!/usr/bin/python3
# Copyright 2023 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import atheris
import sys

import datetime
import croniter

def RandomDateTime(fdp):
    return datetime.datetime.now() + fdp.ConsumeProbability() * datetime.timedelta(days=200000)

def TestOneInput(data):
  fdp = atheris.FuzzedDataProvider(data)
  cron_str = fdp.ConsumeString(50)
  testdate = RandomDateTime(fdp)
  try:
    croniter.croniter.match(cron_str, testdate)
  except croniter.CroniterBadCronError as e:
    pass


def main():
  atheris.instrument_all()
  atheris.Setup(sys.argv, TestOneInput)
  atheris.Fuzz()

if __name__ == "__main__":
  main()
