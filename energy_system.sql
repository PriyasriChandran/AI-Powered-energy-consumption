--
-- Database: `energy_system`
--

-- --------------------------------------------------------

--
-- Table structure for table `building_managers`
--

CREATE TABLE `building_managers` (
  `id` int(11) NOT NULL auto_increment,
  `name` varchar(100) default NULL,
  `email` varchar(100) default NULL,
  `mobile` varchar(15) default NULL,
  `building_name` varchar(100) default NULL,
  `username` varchar(50) default NULL,
  `password` varchar(255) default NULL,
  PRIMARY KEY  (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=3 ;

--
-- Dumping data for table `building_managers`
--

INSERT INTO `building_managers` (`id`, `name`, `email`, `mobile`, `building_name`, `username`, `password`) VALUES
(1, '', '', '', '', '', ''),
(2, 'Raj', 'Raj@gmail.com', '8764312345', 'Building ', 'raj', '1234');

-- --------------------------------------------------------

--
-- Table structure for table `technicians`
--

CREATE TABLE `technicians` (
  `id` int(11) NOT NULL auto_increment,
  `name` varchar(100) default NULL,
  `username` varchar(50) default NULL,
  `password` varchar(255) default NULL,
  `created_by` int(11) default NULL,
  `email` varchar(100) default NULL,
  `mobile` varchar(15) default NULL,
  PRIMARY KEY  (`id`),
  UNIQUE KEY `username` (`username`),
  KEY `created_by` (`created_by`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=2 ;

--
-- Dumping data for table `technicians`
--

INSERT INTO `technicians` (`id`, `name`, `username`, `password`, `created_by`, `email`, `mobile`) VALUES
(1, 'Vijay', 'vijay', '1234', 2, NULL, NULL);

--
-- Constraints for dumped tables
--

--
-- Constraints for table `technicians`
--
ALTER TABLE `technicians`
  ADD CONSTRAINT `technicians_ibfk_1` FOREIGN KEY (`created_by`) REFERENCES `building_managers` (`id`);
