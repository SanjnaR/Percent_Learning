#!/usr/bin/env python
import requests

def main():
    print "Hello Rev.Ai"
    r = requests.get('https://api.rev.ai/revspeech/v1beta/account', headers={'Authorization': 'Bearer <01PQmfvXiLhsyVTwD0RW68lOFqas3STDiYf-RZ6FZgS9_z29DicZNhOA3y5JMBTDK_KM3ODdu0c-EIjd842MtsXwTNTks>'})
    print(r.text)

if __name__ == '__main__':
  main()