#   Copyright 2022 hidenorly
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.

import sys
import os
import argparse
import unicodedata
import pandas as pd
import tabula

def ljust_jp(value, length, pad = " "):
  count_length = 0
  for char in value.encode().decode('utf8'):
    if ord(char) <= 255:
      count_length += 1
    else:
      count_length += 2
  return value + pad * (length-count_length)

def isRobustNumeric(data):
  try:
    float(data)
  except ValueError:
    return False
  else:
    return True

def getCsvJsonCommon(row):
  result = ""

  for aData in row:
    if result != "":
      result = result + ", "
    if isRobustNumeric(aData):
      if pd.isnull(aData):
        aData = "\"\""
      result = result + str(aData)
    else:
      result = result + "\"" + aData + "\""

  return result

def getCsv(row):
  result = getCsvJsonCommon(row) + ","
  return result

def getJson(row):
  result = "[ " + getCsvJsonCommon(row) + " ],"
  return result


if __name__=="__main__":
  parser = argparse.ArgumentParser(description='Parse command line options.')
  parser.add_argument('args', nargs='*', help='Specify pdf files e.g. pdf1.pdf pdf2.pdf')
  parser.add_argument('-j', '--json', action='store_true', default=False, help='Output as json')
  parser.add_argument('-c', '--csv', action='store_true', default=False, help='Output as csv')
  parser.add_argument('-m', '--merge', action='store_true', default=False, help='Output table as merged')

  args = parser.parse_args()

  if not args.json and not args.csv:
    args.csv=True

  if args.json and args.merge:
    print("[")
  for aPdfFile in args.args:
    if os.path.exists( aPdfFile ):
      dfs = tabula.read_pdf( aPdfFile, lattice=True, silent=True, pages='all' )
      for df in dfs:
        if args.json and not args.merge:
          print("[")
        for index, row in df.iterrows():
          if args.json:
            print( "  " + getJson(row) )
          elif args.csv:
            print( getCsv(row) )
        if args.json and not args.merge:
          print("]")
    if not args.merge:
      print("")
  if args.json and args.merge:
    print("]")
