using System;
using System.Collections.Generic;
using System.Text;

namespace DataStructureDemo.Classes
{
    public class SingleLinkedList
    {
        public SingleLinkedNode Head { get; set; }
        public SingleLinkedNode Last { get; set; }
        public int Length { get; set; }
        public SingleLinkedList()
        {
        }
        public void DisplayList()
        {
            if (Head == null)
            {
                Console.WriteLine("No List defined");
                return;
            }
            SingleLinkedNode nextNode = Head;
            while (nextNode != null)
            {
                Console.Write($"|{nextNode.Value}| --> ");
                nextNode = nextNode.Next;
            }
            Console.WriteLine();
        }
        public void Add(SingleLinkedNode newNode)
        {
            if (Head == null)
            {
                Head = newNode;
            }
            else
            {
                SingleLinkedNode nextNode = Head;
                while (nextNode.Next != null)
                {
                    nextNode = nextNode.Next;
                }
                nextNode.Next = newNode;
                Last = newNode;
            }
                            Length += 1;
        }
        public void AddStart(SingleLinkedNode newNode)
        {
            if(Head == null)
            {
                Head = newNode;
                Length += 1;
                return;
            }
            newNode.Next = Head;
            Head = newNode;
            Length += 1;
        }
        public void AddAfter(SingleLinkedNode prevNode, SingleLinkedNode newNode)
        {
            SingleLinkedNode track = Head;
            while (track.Value != prevNode.Value)
            {
                track = track.Next;
            }
            if(track.Next != null)
            {
                newNode.Next = track.Next;
                track.Next = newNode;
            }
            else
            {
                track.Next = newNode;
                Last = track.Next;
            }
            Length += 1;


        }
        public void AddBefore(SingleLinkedNode nextNode, SingleLinkedNode newNode)
        {
            SingleLinkedNode track = Head;
            SingleLinkedNode cacheprev = null;
            while (track.Value != nextNode.Value)
            {
                cacheprev = track;
                track = track.Next;
            }

            newNode.Next = track;
            cacheprev.Next = newNode;
            Length += 1;
        }
        public void DeleteIndex(int i)
        {
            if (i >= Length)
            {
                Console.WriteLine("Index not found!");
                return;
            }
            
            if (i == 0)
            {
                Head = Head.Next;
                Length -= 1;
                return;
            }

            SingleLinkedNode track = Head;
            
            for(int ind = 0; ind <= i; ind++)
            {
                if(ind == i - 1)
                {
                    if (track.Next.Next == null)
                    {
                        track.Next = null;
                        Last = track;
                        return;
                    }
                   
                    else
                    {
                        track.Next = track.Next.Next;
                        break;
                    }
                }

                track = track.Next;   
            }
            
            if(Last == null)
            {
                Last = track.Next.Next;
            }
            
            Length -= 1;
        }
        public void DeleteValue(int i)
        {
            SingleLinkedNode track = Head;
            SingleLinkedNode cache = new SingleLinkedNode(0);
            SingleLinkedNode cache2 = new SingleLinkedNode(0);
            while (track.Value != i)
            {
                cache = track;
                track = track.Next;
            }
            cache2 = track.Next;
            cache.Next = cache2;
            track = null;
            if (Last == null)
            {
                Last = cache2;
            }
            Length -= 1;
        }
        public void Clear()
        {
            Head = null;
            Last = null;
            Length = 0;
        }
        public bool Contains(int value)
        {
            SingleLinkedNode track = Head;
            while (track != null)
            {
                if(track.Value == value)
                {
                    return true;
                }
                track = track.Next;
            }
            return false;
        }
        public int Find(int value)
        {
            SingleLinkedNode track = Head;
            int index = 0;
            while (track != null)
            {
                if (track.Value == value)
                {
                    return index;
                }
                track = track.Next;
                index++;
            }
            Console.Write("No Value found: ");
            return -1;
        }
    }
}
