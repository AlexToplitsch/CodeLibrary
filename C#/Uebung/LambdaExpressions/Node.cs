using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace LambdaExpressions
{
    public class Node<T> // generische Klasse
    {
        public Node<T> PrevNode { get; set; }
        public Node<T> NextNode { get; set; }
        public T Value { get; set; } // Property mit dem übergebenen Datentyp
    }
}
